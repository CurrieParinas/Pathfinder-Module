from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, null=True)
    slug = models.SlugField(null=True)
    x = models.IntegerField()
    y = models.IntegerField()
    floorNumber = models.IntegerField(default = 1)
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name   