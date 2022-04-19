import bcrypt
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
    def band_validator(self,postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name']="name must be above 2 "
        if len(postData['music']) < 2:
            errors['music']="music must be above 2 "
           
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

class Band(models.Model):
    name=models.CharField(max_length=45)
    music=models.CharField(max_length=45)
    city=models.CharField(max_length=45)
    member=models.ForeignKey(User,related_name="bands",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

def create_user(info):
    password = info['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()  
    print(pw_hash)      
    User.objects.create(first_name=info['first_name'],last_name=info['last_name'],email=info['email'],password=pw_hash )

def create_band(info):
    user=int(info['band'])
    print(type(user))
    user_id=User.objects.get(id=user)
    Band.objects.create(name=info['name'],music=info['music'],city=info['city'],member=user_id)

def all_user():
    return User.objects.all()

def all_band():
    return Band.objects.all()

def get_user(info):
    return User.objects.get(id=info)

def get_band(info):
    return Band.objects.get(id=info)

def updateband(info,info_id):
    band=Band.objects.get(id=info_id)
    band.name=info['name']
    band.music=info['music']
    band.city=info['city']
    band.save()

def delete_band(info):
    band=Band.objects.get(id=info['del_band'])
    band.delete()
    