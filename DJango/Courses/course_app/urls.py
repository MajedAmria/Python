from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('add',views.add),
    path('courses/destroy/<int:id>',views.to_delete),
    path('delete',views.delete),
    path('no',views.no)
]