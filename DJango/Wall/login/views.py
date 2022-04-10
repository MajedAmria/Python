import bcrypt
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
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
            
                return redirect('/wall')
            else:
                messages.error(request,"incorrect password") 
                  
    return redirect('/wall')
    
