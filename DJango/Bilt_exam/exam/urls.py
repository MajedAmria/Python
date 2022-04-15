from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('regestration',views.regestration),
    path('login',views.login),
    path('car',views.showcar),
    path('delete',views.logout),
    path('add',views.create_car),
    path('new',views.add_car_to_sale),
    path('view/<int:carid>',views.view),
    path('edit/<int:carid>',views.edit),
    path('update',views.update_car),
    path('delete_car',views.delete_car)

 
]