from django.contrib import admin
from .models import Professor, Time, Schedule, Course, Session, CourseCombo

# Register your models here.
admin.site.register(Time)
admin.site.register(Schedule)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(CourseCombo)
admin.site.register(Professor)