from django.db import models
 
# Create your models here.
 
class registeruser(models.Model):
    username = models.IntegerField()
    email = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    cpassword = models.CharField(max_length=50,default='')
    def __str__(self):
        return self.username
 
    userAuth_objects = models.Manager()
