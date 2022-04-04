from django.db import models

class Book(models.Model):
        title = models.CharField(max_length=255)
        desc=models.TextField(default="book discription")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class Author(models.Model):
        firs_name = models.CharField(max_length=255)
        last_name=models.CharField(max_length=255)
        note=models.TextField(default="")
        books = models.ManyToManyField(Book, related_name="authors")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

def list_of_all_books():
    return Book.objects.all()

def create_book(info):
    Book.objects.create(title=info['title'], desc=info['desc'])

def add_auth_to_book(info,book_id):
        thisBook = Book.objects.get(id=book_id)
        thisAuthor = Author.objects.get(id=info['auth_id'])
        thisBook.authors.add(thisAuthor)

def list_of_all_authors():
    return Author.objects.all()

def create_author(info):
    selected_book = int(info['authors'])
    this_book = Book.objects.get(id=selected_book)
    Author.objects.create(first_name=info['firs_name'], last_name=info['last_name'],note=info['note'],books=this_book)
def add_book_to_auth(info,author_id):
        thisAuthor = Author.objects.get(id=author_id)
        thisBook = Book.objects.get(id=info['book_id'])
        thisAuthor.books.add(thisBook)