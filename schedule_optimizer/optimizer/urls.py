from django.urls import path, re_path

from . import views

urlpatterns = [
    #get
    path("all/professors/", views.getAllProfessors, name="getAllProfessors"),
    path("all/schedules/", views.getAllSchedules, name="getAllSchedules"),
    path("isloggedin/", views.isLoggedIn, name="isLoggedIn"),
    path("getschedules/", views.getSchedules, name="getSchedules"),

    re_path(r'^generate/$', views.generateSchedule, name='generateSchedule'),
    
    #post
    path("add/professor/", views.addProfessor, name="addProfessor"),
    path("add/schedule", views.addSchedule, name="addSchedule")
]
