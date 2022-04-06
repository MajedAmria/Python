from django.shortcuts import render,redirect 

from .models import *

def index(request):
    listall=all_courses()
    context={
        'courses':listall
    }
    return render(request,"index.html",context)
def add(request):
    creat_course(request.POST)
    return redirect('/')

def to_delete(request):
    course=remove_course(request.POST)
    context={
        'course_name':course.name,
        'course_desc':course.desc
    }
    return render(request,"delete.html",context)

def delete(request):
    x=remove_course(request.POST)
    x.delete()
    return redirect('/')

def no(request):
    return redirect('/')