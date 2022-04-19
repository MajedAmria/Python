from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('regestration',views.regestration),
    path('login',views.login),
    path('success',views.sucsses),
    path('newband',views.newband),
    path('addnewband',views.addnewband),
    path('mybands',views.myband),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('deleteband',views.delete),
    path('delete',views.logout)
 
]