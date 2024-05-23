from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    college = models.CharField(max_length=300,default = "College of Arts and Sciences")
    building =  models.CharField(max_length=300,default="Rizal Hall")
    x = models.IntegerField()
    y = models.IntegerField()
    floorNumber = models.IntegerField(default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name   
    
class College(models.Model):
    name = models.CharField(max_length=300,null=True,unique=True)
    slug = models.SlugField(null=True, max_length=300)

    def __str__(self):
        return self.name
    
class Building(models.Model):
    name = models.CharField(max_length=300,null=True)
    college = models.CharField(max_length=300,null=True)
    slug = models.SlugField(null=True, max_length = 300)

    def __str__(self):
        return self.name
    
    