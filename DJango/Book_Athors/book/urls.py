
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book),
    path('add',views.book_info),
    path('author',views.author),
    path('add_author',views.author_info),
    path('books/<int:bookid>',views.showbook),
    path('authors/<int:authorid>',views.showauthor),
    path('authors',views.Add_book_to_author),
    path('books',views.Add_author_to_book),
   
]