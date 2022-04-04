
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book),
    path('add',views.book_info),
    path('author',views.author),
    path('add_author',views.author_info),
    # path('authors/<int:author.id>',views.print_author),
    # path('books/<int:book.id>',views.print_book)
]