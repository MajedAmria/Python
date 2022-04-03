from django.shortcuts import render,redirect
from .models import *
from . import models

def show(request):
    list_of_dojos = models.list_of_all_dojos()
    list_of_ninja = models.list_of_all_ninja()
    
    context = {
        "dojo_list" : list_of_dojos,
        "ninja_list" : list_of_ninja,
    }
    return render(request,"index.html",context)
def ninja_info(request):
    # print(request.POST)
    create_ninja(request.POST)

    return redirect("/")

def dojo_info(request):
    creat_dojo(request.POST)
    return redirect("/")