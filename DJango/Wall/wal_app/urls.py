from django.urls import path
from . import views

urlpatterns = [
    path('wall', views.wall),
    path('post_message',views.post_message),
    path('post_comment/<int:msg_id>', views.post_comment),
    path('user_posts/<int:user_id>', views.user_posts),
    path('wall',views.sucsses),
    path('delete',views.logout),
]