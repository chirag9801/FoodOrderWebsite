from django.db import models

# Create your models here.
class order(models.Model):
    name=models.CharField(max_length=50)
    number=models.IntegerField()
    food=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    

    def __str__(self):
        return self.name
#new class
class userregister(models.Model):
    fullname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    num=models.IntegerField()
    
    def __str__(self):
        return self.fullname