
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book),
    path('add',views.book_info),
    path('author',views.author),
    path('add_author',views.author_info),
    path('books/<int:bookid>',views.showbook),
    path('authors/<int:auhtorid>',views.showauthor),
    path('books',views.book_to_author),
    path('authors',views.author_to_book),
   
]