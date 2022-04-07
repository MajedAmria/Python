from email import message
from email.message import Message
from django.db import models

from login.models import User

class Message(models.Model):
    message = models.TextField(max_length=255)
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    title = models.TextField(max_length=255)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_message(info):
    selected_user = int(info['user'])
    this_user = User.objects.get(id=selected_user)
    Message.objects.create(message=info['message'], dojo=this_user)

def get_message(info):
    return Message.objects.get(id=info['id'])
# def create_comment(info):
#     selected_dojo = int(info['dojo'])
#     this_dojo = Dojo.objects.get(id=selected_dojo)
#     Ninja.objects.create(first_name=info['first_name'], last_name=info['last_name'], dojo=this_dojo)