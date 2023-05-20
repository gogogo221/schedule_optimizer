from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=100,  unique=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    num_ratings = models.IntegerField()
    difficulty = models.DecimalField(max_digits=5, decimal_places=1)
    def __str__(self):
        return f"{self.name}, rating: {self.rating}, number of ratings: {self.num_ratings}"

class Time(models.Model):
    day = models.CharField(max_length=10)
    start = models.CharField(max_length=10)
    end = models.CharField(max_length=10) 
    def __str__(self):
        return f"{self.day}, {self.start}, {self.end}"

class Schedule(models.Model):
    user = models.ForeignKey(User, related_name="schedules", on_delete=models.CASCADE, null=True)
    units = models.IntegerField()
    def __str__(self):
        return f""

class Course(models.Model):
    name = models.CharField(max_length=150, unique=True) #software engineering
    tag = models.CharField(max_length=50) #CSCI-201
    units = models.IntegerField()#4
    schedule = models.ForeignKey(Schedule, related_name="courses", on_delete=models.CASCADE)
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

class CourseCombo(models.Model):
    schedule = models.ForeignKey(Schedule, related_name="course_combos", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="course_combos", on_delete=models.CASCADE)
    sessions = models.ManyToManyField(Session)
    units = models.IntegerField()
    times = models.ManyToManyField(Time)