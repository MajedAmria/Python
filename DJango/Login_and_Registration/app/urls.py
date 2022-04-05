from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('regestration',views.regestration),
    path('login',views.login),
    path('success',views.sucsses),
    path('delete',views.logout)
 
]