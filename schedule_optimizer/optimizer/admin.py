from django.contrib import admin
from .models import Professor, Schedule

# Register your models here.

admin.site.register(Schedule)
admin.site.register(Professor)