from django.db import models

class A(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.TextField(max_length=45)
    email_adress = models.TextField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
