from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    x = models.IntegerField()
    y = models.IntegerField()
    floor = models.IntegerField()
    date_created = models.DateTimeField(default=timezone.now)
    date_modified = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name   