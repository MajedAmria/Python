from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length=45)
    city = models.TextField(max_length=45)
    state = models.TextField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Ninja(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.TextField(max_length=45)
    dojo=models.ForeignKey(Dojo, related_name="ninjas", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def list_of_all_dojos():
    return Dojo.objects.all()
def list_of_all_ninja():
    return Ninja.objects.all()

def create_ninja(info):
    selected_dojo = int(info['dojo'])
    this_dojo = Dojo.objects.get(id=selected_dojo)
    Ninja.objects.create(first_name=info['first_name'], last_name=info['last_name'], dojo=this_dojo)
def creat_dojo(info):
    Dojo.objects.create(name=info['name'],city=info['city'],state=info['state'])