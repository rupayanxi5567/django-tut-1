from django.db import models

# Create your models here.

class students(models.Model):
    name = models.CharField(max_length=400)
    college = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    age = models.IntegerField(max_length=3)
    is_active = models.BooleanField(default=True)