from django.db import models

class Book(models.Model):
        title = models.CharField(max_length=255)
        desc=models.TextField(default="book discription")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
        first_name = models.CharField(max_length=255)
        last_name=models.CharField(max_length=255)
        note=models.TextField(default="")
        books = models.ManyToManyField(Book, related_name="authors")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

def list_of_all_books():
    return Book.objects.all()

def create_book(info):
    Book.objects.create(title=info['title'], desc=info['desc'])
def show_book(book_id):
    x=Book.objects.get(id=book_id)
    # x.title=info['title']


def add_auth_to_book(info,book_id):
        thisBook = Book.objects.get(id=book_id)
        thisAuthor = Author.objects.get(id=info['auth_id'])
        thisBook.authors.add(thisAuthor)

def list_of_all_authors():
    return Author.objects.all()

def create_author(info):
    Author.objects.create(first_name=info['first_name'], last_name=info['last_name'],note=info['note'])
def add_book_to_auth(info,author_id):
        thisAuthor = Author.objects.get(id=author_id)
        thisBook = Book.objects.get(id=info['book_id'])
        thisAuthor.books.add(thisBook)
def show_author(auhtor_id):
    x=Author.objects.get(id=auhtor_id)
