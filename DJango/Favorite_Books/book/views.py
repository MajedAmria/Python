import bcrypt
from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request,"index.html")


def edit(request,bookid):
    user=User.objects.get(email=request.session['email'])
    users=User.objects.all()
    context={
        'firstname': user.first_name,
        'user_id':user.id,
        'all_user':users,
        'book':Book.objects.get(id=bookid)
    }
    return render(request,"edit.html",context)

 

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
            
                return redirect('/book')
            else:
                messages.error(request,"incorrect password") 
                  
    return redirect('/')

def show(request):
    users=User.objects.all()
    book= Book.objects.all()
      
   
    
    context={
            'list_book':book,
            'list_user':users,
                }
    return render(request,"show.html",context)
    
def book(request):
    if  'email' in request.session :
      user=User.objects.get(email=request.session['email'])
      users=User.objects.all()
      book= Book.objects.all()
      
   
    
      context={
            'firstname': user.first_name,
            'lastname':user.last_name,
            'user':user,
            'list_book':book,
            'list_user':users,
                }
    
      return render(request,"book.html",context) 
    else:
      return redirect('/')

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
      
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/book')
    user=User.objects.get(email=request.session['email'])
    selected_user = user.id
    this_user = User.objects.get(id=selected_user)
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'], book_upload=this_user)
    last_book=Book.objects.last()
    user.users.add(last_book)
    return redirect('/book')

def update(request):
    errors = Book.objects.book_validator(request.POST)
    this_book_id = request.POST['this_book_id']
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/book/'+str(this_book_id))
    else:
        x=Book.objects.get(id=this_book_id)
        x.title=request.POST['title']
        x.desc=request.POST['desc']
        x.save()
        return redirect('/book') 

def add_favorete(request):
    this_book_id = request.POST['this_book_id']
    user_id=request.session['user_id']
    bookobject=Book.objects.get(id=this_book_id)
    this_user=User.objects.get(id=user_id)
    bookobject.users.add(this_user)
    
    return redirect('/book')

def remove_favorate(request):
    this_book_id = request.POST['this_book_id']
    user_id=request.session['user_id']
    bookobject=Book.objects.get(id=this_book_id)
    this_user=User.objects.get(id=user_id)
    bookobject.users.remove(this_user)
    
    return redirect('/book')

def delete(request):
    this_book_id = request.POST['this_book_id']
    x=Book.objects.get(id=this_book_id)
    x.delete()
    return redirect('/book') 

def logout(request):
    del request.session['email']
    
    return redirect('/')