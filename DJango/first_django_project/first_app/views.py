from django.shortcuts import  HttpResponse, redirect
from django.http import JsonResponse


# Create your views here.
def index(request):
    return HttpResponse("placeholder to display a new form to create a new blog ")
def root(request):
    return HttpResponse("placeholder to display a new form to create a new blog")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog ")
def create(request):
    return redirect("/")

def show(request,num):
    return HttpResponse("placeholder to display a new form to create a new blog %d" %(num))
def edit(request, number):
    return HttpResponse("placeholder to edit blog %d" %(number))
def destroy(request,num):
    return redirect("/blogs")

def jason(request):
    return JsonResponse({"title": "My_first_blog", "content":"lorem Majed Amira Hana Albidaq"})