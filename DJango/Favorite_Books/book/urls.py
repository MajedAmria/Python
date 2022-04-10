
from django.urls import path
from . import views
#localhost:8000/
urlpatterns = [
    path('',views.index),
    path('book',views.book),
    path('regestration',views.regestration),
    path('login',views.login),
    path('logut',views.logout),
    path('create',views.add_book),
    path('book/<int:bookid>',views.edit),
    path('book_update',views.update),
    path('delete',views.delete),
    path('book/<int:bookid>',views.show)
]