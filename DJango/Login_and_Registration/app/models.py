from django.db import models
import re

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "Blog first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Blog last name should be at least 3 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        new_user_email=User.objects.filter(email=postData['email'])
        if len(new_user_email):
            errors['email']="email is already exsist"
        if len(postData['password']) < 8:
            errors["password"] = "Blog password should be at least 8 characters" 
        if postData['password'] != postData['confirm']:
            errors["confirm"] = "Not confirm password"    
        return errors


    def login_validator(self,postData):
        user = User.objects.filter(email=postData['email']) 
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if not len(user):
            errors['email']="email is not valid"
        if len(postData['password']) < 8:
            errors['password'] = "Blog password should be at least 8 characters"
           
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()



