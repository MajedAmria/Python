import bcrypt
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from . import models
from django.contrib import messages


def index(request):
    return render(request,"index.html")

def regestration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
    print(pw_hash)      

    if request.POST['which_form'] == 'register':
        create_user(request.POST)
    return redirect('/')

def login(request):
    errors = User.objects.login_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    if request.POST['which_form'] == 'login':
        user = User.objects.get(email=request.POST['email']) 
        
        if user is not None:
            logged_user = user 
            
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            
                request.session['email'] = logged_user.email
                request.session['user_id']=logged_user.id
            
                return redirect('/success')
            else:
                messages.error(request,"incorrect password") 
                  
    return redirect('/')
    
def sucsses(request):
    if  'email' in request.session :
      user=User.objects.get(email=request.session['email']) 
      alluser=all_user()
      allbands=all_band()
      user_band=get_user(user.id)
      context={
            'firstname': user.first_name,
            'userid': user.id,
            'users': alluser,
            'bands' : allbands,
            'inuser':user_band
                }
    
      return render(request,"Band.html",context) 
    else:
      return redirect('/')

def newband(request):
    user=User.objects.get(email=request.session['email']) 
    context={
            'firstname': user.first_name,
            'userid': user.id,
            
                }
    
    return render(request,"new.html",context)

def addnewband(request):
    errors = Band.objects.band_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/newband')
    else:    
       create_band(request.POST)
       return redirect('/success')

def myband(request):
    user=User.objects.get(email=request.session['email']) 
    allbands=all_band()
    alluser=all_user()
    user_band=get_user(user.id)
   
    context={
            'firstname': user.first_name,
            'userid': user.id,
            'users': alluser,
            'bands':allbands,
            'inuser':user_band
            
                }
    return render(request,"myband.html",context)

def edit(request, id):
    user=User.objects.get(email=request.session['email']) 
    get_user(id)
    band=get_band(id)
    allbands=all_band()
    context={
            'firstname': user.first_name,
            'userid': user.id,
            'bands':allbands,
            'band':band
    }
    return render(request,"edit.html",context)

def update(request, id):
    errors = Band.objects.band_validator(request.POST)
      
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+str (id))
    get_band(id)
    updateband(request.POST,id)
    return redirect('/success')

def delete(request):
    
    models.delete_band(request.POST)
    return redirect('/success')

def logout(request):
    del request.session['email']
    
    return redirect('/')