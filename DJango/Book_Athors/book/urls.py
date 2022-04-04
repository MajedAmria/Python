
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book),
    path('add',views.book_info),
    path('author',views.author),
    path('add_author',views.author_info),
    path('authors/<int:book.id>',views.showbook),
   
]