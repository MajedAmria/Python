from django.db import models
class Show(models.Model):
    title=models.CharField(max_length=254)
    Network=models.CharField(max_length=254)
    release_Date=models.DateField(auto_now_add=True)
    discription=models.TextField(default="Nice")
    crreated_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
