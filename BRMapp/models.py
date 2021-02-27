from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=100)
    price=models.FloatField()
    author=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)

class BRMuser(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) 
    nickname=models.CharField(max_length=20,null=False)
#in django 2 we put models.CASCADE in
#double quotes but in django 3 it is not possible.
