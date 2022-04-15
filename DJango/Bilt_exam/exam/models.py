from ast import Return
from django.db import models
import re

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 3:
            errors["first_name"] = "Blog first name should be at least 2 characters"
        if len(postData['last_name']) < 3:
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

    def add_validator(self,postData):
        errors = {}
        if postData['price'] <= 0:
            errors['price'] = "price canot be zero"
        if postData['year'] <= 0:
            errors['yaer'] = "yaer canot be zero"
           
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()

class Car(models.Model):
    model=models.CharField(max_length=45)
    year=models.IntegerField()
    price=models.FloatField(max_length=45)
    maker=models.CharField(max_length=45)
    desc=models.TextField(max_length=100)
    seller=models.ForeignKey(User,related_name="cars" ,on_delete=models.CASCADE)
    objects = BlogManager()

def add_car(info):
    
    selected_user = int(info['user'])
    this_user = User.objects.get(id=selected_user)
    Car.objects.create(model=info['model'], year=info['year'], price=info['price'],maker=info['maker'],desc=info['desc'],seller=this_user)

def list_car():
    return Car.objects.all()  

def list_user():
    return User.objects.all()
def getseller(info):
    return User.objects.get(id=info['id'])
def getcar(info):
    return Car.objects.get(id=info['id'])

def update(info):
  
    this_book_id = info['this_book_id']
 
    car=Car.objects.get(id=this_book_id)
    car.price=info['price']
    car.model=info['model']
    car.meker=info['meker']
    car.year=info['year']
    car.desc=info['desc']
    car.save()
       

def delete(info):
    this_book_id = info['id']
    car=Car.objects.get(id=this_book_id)
    return car.delete()
