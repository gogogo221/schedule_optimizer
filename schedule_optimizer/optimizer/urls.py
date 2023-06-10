from django.urls import path, re_path

from . import views

urlpatterns = [
    #get
    path("all/times/", views.getAllTimes, name="getAllTimes"),
    path("all/professors/", views.getAllProfessors, name="getAllProfessors"),
    path("all/sessions/", views.getAllSessions, name="getAllSessions"),
    path("all/courses/", views.getAllCourses, name="getAllCourses"),
    path("all/course_combos/", views.getAllCourseCombos, name="getAllCourseCombos"),
    path("all/schedules/", views.getAllSchedules, name="getAllSchedules"),

    re_path(r'^generate/$', views.generateSchedule, name='generateSchedule'),
    
    #post
    path("add/professor/", views.addProfessor, name="addProfessor"),
]
