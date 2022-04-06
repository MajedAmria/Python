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

def showbook(request,bookid):
    context={
        'book':models.show_book(bookid),
        'remaining_authors': models.book(bookid),
    }
    return render(request, "book_info.html",context)

def showauthor(request,authorid):
    context={
        'author':models.show_author(authorid),
        'remaining_books':models.author(authorid),
    }
    return render(request, "author_info.html",context)

def Add_book_to_author(request):
    book_id=request.POST['book']
    author_id=request.POST['author_id']

    models.add_book_to_auth(author_id,book_id)
    return redirect('authors/'+str(author_id))

def Add_author_to_book(request):
    book_id=request.POST['book_id']
    author_id = request.POST['author']
    models.add_auth_to_book(author_id,book_id)
    return redirect('books/'+str(book_id))