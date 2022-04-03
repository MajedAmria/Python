from django.urls import path
from . import views

urlpatterns = [
    path('',views.show),
    path('ninja',views.ninja_info),
    path('dojo',views.dojo_info),


]