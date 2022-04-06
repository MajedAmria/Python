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
    return Book.objects.create(title=info['title'], desc=info['desc'])

def show_book(book_id):
    x=Book.objects.get(id=book_id)
    return x
  
def add_auth_to_book(author_id,book_id):
        thisBook = Book.objects.get(id=book_id)
        # thisAuthor = Author.objects.get(id=info['author_id'])
        thisAuthor = Author.objects.get(id=author_id)
        return thisBook.authors.add(thisAuthor)

def list_of_all_authors():
    return Author.objects.all()

def create_author(info):
    return Author.objects.create(first_name=info['first_name'], last_name=info['last_name'],note=info['note'])

def add_book_to_auth(auther_id,book_id):
        thisAuthor = Author.objects.get(id=auther_id)
        thisBook = Book.objects.get(id=book_id)
        return thisAuthor.books.add(thisBook)

def show_author(auhtor_id):
    x=Author.objects.get(id=auhtor_id)
    return x

def book(book_id):
    selected_book = Book.objects.get(id=book_id)
    return Author.objects.exclude(id__in = selected_book.authors.all() )

def author(author_id):
    selected_author = Author.objects.get(id=author_id) 
    return Book.objects.exclude(id__in=selected_author.books.all())
   
