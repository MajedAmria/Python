from django.urls import path     
from . import views
urlpatterns = [
    path('', views.show),
    path('show',views.index),	   
]