from django.urls import path
from . import views
urlpatterns = [
  path('',views.display),
  path('clear',views.destroy),
  path('clear',views.reset),
  path('add',views.add_two),


  
]