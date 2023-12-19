from django.db import models

# Create your models here.

class emps(models.Model):
    name = models.CharField(max_length=400)
    emps_id = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    phone = models.IntegerField(max_length=13)
    is_working = models.BooleanField(default=True)
    dept = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    
    


class testimonial(models.Model):
    name = models.CharField(max_length=200)
    testimonial = models.TextField()
    pictures = models.ImageField(upload_to="testimonials/")
    rating = models.IntegerField()

    def __str__(self):
        return self.testimonial


