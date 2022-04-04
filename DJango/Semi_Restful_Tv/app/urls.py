from . import views
from django.urls import path


urlpatterns = [
    path('shows', views.index),
    path('shows/new', views.addNewShow),
    path('shows/creat',views.insertShow),
    path('shows/<int:Showid>',views.show),
    path('shows/<int:showid>/edit',views.edit),
    path('shows/<int:showid>/delete',views.delete),
    # delete
    path('shows/<int:showid>/update',views.update),

]