from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=100,  unique=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    num_ratings = models.IntegerField(null=True, blank=True)
    difficulty = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)
    def __str__(self):
        return f"{self.name}, rating: {self.rating}, number of ratings: {self.num_ratings}"


class Schedule(models.Model):
    user = models.ForeignKey(User, related_name="schedules", on_delete=models.CASCADE, null=True, blank=True)
    course_data = models.CharField(max_length=10000)
    semester = models.CharField(max_length=10)
    units= models.IntegerField()    
    def __str__(self):
        return f""

    
