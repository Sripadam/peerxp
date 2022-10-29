from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from django.utils.timezone import now
# Create your models here.
#/class User(AbstractUser):
    #is_admin = models.BooleanField('Is admin',default = True)
    
    #name = models.TextField()
    #phone = models.IntegerField()
    #email = models.TextField()
    #password = models.TextField()
    #Department = models.TextField()
    #Role = models.TextField()
    #def __str__(self):
        #return str(self.name)/#

class Ticket(models.Model):
    subject= models.TextField()
    body = models.TextField()
    priority = models.TextField()
    def __str__(self):
        return str(self.subject)      
class Department(models.Model):
    name = models.TextField()
    description = models.TextField()
    created_by = models.ForeignKey(User,on_delete =models.CASCADE)
    last_update = models.DateTimeField()
    def __str__(self):
        return str(self.created_by) +  " created: " + str(self.Name)
