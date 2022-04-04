from django.shortcuts import render,redirect

from .models import *
from . import models

def book(request):
    list_of_book = models.list_of_all_books()
    context = {
        "book_list" : list_of_book,
    }
    return render(request,"index.html",context)
def author(request):

    list_of_author = models.list_of_all_authors()
    
    context = {
        "author_list" : list_of_author,
    }
    return render(request,"index2.html",context)
def book_info(request):
    create_book(request.POST)
    return redirect("/")

def author_info(request):
    create_author(request.POST)
    return redirect("/author")

