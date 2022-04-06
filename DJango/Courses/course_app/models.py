from django.db import models

class Course(models.Model):
    name=models.CharField(max_length=45)
    desc=models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def creat_course(info):
    Course.objects.create(name=info['name'],desc=info['desc'])
def all_courses():
    return Course.objects.all()
def remove_course(info):
    return Course.objects.get(id=info['id'])
    
     
