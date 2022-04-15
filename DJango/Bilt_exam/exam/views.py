import bcrypt

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
        User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash )
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
            
                return redirect('/car')
            else:
                messages.error(request,"incorrect password") 
                  
    return redirect('/')
    

    
def logout(request):
    del request.session['email']
    
    return redirect('/')

def showcar(request):
    user=User.objects.get(email=request.session['email'])

    if  'email' in request.session :
        listofuser=models.list_user()
        listofcar=models.list_car()
        context={
        'cars': listofcar,
        'firstname':user.first_name,
        'user':user,
        'users':listofuser,
                }
        return render(request,"car.html",context)
    else:
      return redirect('/')

def create_car(request):


    add_car(request.POST)

    return redirect('/car')

def add_car_to_sale(request):
    user=User.objects.get(email=request.session['email'])
    userid=user.id
    context={
        'user':userid
    }
    return render(request,"newcar.html",context)

def edit(request,carid):
    cars=getcar(request.POST[carid])
    
    context={
        'car':cars,
    }
    return render(request,"edit.html",context)

def update_car(request):
    errors = User.objects.add_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    update(request.POST)
    return redirect('/car')

def view(request,carid):
    cars=getcar(request.POST[carid])
    seller=getseller()
    context={
        'car':cars,
        'seller':seller,
    }
    return render(request,"showcar",context)

def delete_car(request):
    delete(request.POST)
    return redirect('/car')
