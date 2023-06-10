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



class Time(models.Model):
    day = models.CharField(max_length=10)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10) 
    def __str__(self):
        return f"{self.day}, {self.start}, {self.end}"


class Course(models.Model):
    name = models.CharField(max_length=150, unique=True) #software engineering
    tag = models.CharField(max_length=50) #CSCI-201
    units = models.IntegerField()#4
    semester = models.IntegerField()

    class Meta:
        unique_together = ('tag', 'semester',)
    def __str__(self):
        return f"{self.id}, {self.name}, {self.units}"

class Session(models.Model):
    id = models.IntegerField(primary_key = True, unique=True)
    course = models.ForeignKey(Course, related_name="sessions", on_delete=models.CASCADE)
    time = models.OneToOneField(Time, related_name="time",  on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, related_name="sessions_taught", on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    capacity = models.IntegerField()
    registered = models.IntegerField()
    dclearence = models.BooleanField()

    def __str__(self):
        return f"{self.id}, {self.time}, {self.professor}"


class Schedule(models.Model):
    user = models.ForeignKey(User, related_name="schedules", on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f""
class CourseCombo(models.Model):
    #maybe schedule is many to many
    course = models.ForeignKey(Course, related_name="course_combos", on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Session)
    times = models.ManyToManyField(Time)
    schedules = models.ManyToManyField(Schedule, related_name="course_combos", null=True)


        
    
