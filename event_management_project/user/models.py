from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):   #
    password = models.CharField(max_length=128, )
    username = models.CharField(max_length=128, unique=True, null= False)
    first_name = models.CharField(blank=True, max_length=150,)
    last_name = models.CharField(blank=True, max_length=150, )
    email= models.EmailField(blank=True, max_length=254,unique=True)
    mobile_number= models.CharField(max_length=12, unique=True)
         
   
    def __str__(self):
        return self.username