from django.shortcuts import render,redirect

from wal_app.models import create_message

def index(request):
    return render(request,"dashbord.html")

def message(request):
    
    create_message(request.POST)

    return redirect("/")
