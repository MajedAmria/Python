from django.db import models
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title1']) < 2:
            errors["title1"] = "Blog title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"    
        return errors


class Show(models.Model):
    title=models.CharField(max_length=254)
    Network=models.CharField(max_length=254)
    release_Date=models.DateField(auto_now_add=True)
    discription=models.TextField(default="Nice")
    crreated_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    objects = BlogManager()

