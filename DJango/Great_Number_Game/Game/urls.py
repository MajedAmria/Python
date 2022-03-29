from django.urls import path
from . import views
urlpatterns = [
    path('',views.show),
    path('guess',views.guess),
    path('destroy',views.destroy),
]