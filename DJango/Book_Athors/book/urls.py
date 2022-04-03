
from django.urls import path
from . import views

urlpatterns = [
    path('',views.book),
    path('add',views.book_info),
    path('author',views.author),
    # path('author',views.author),
]