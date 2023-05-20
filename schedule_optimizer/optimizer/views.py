from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Professor, Time, Schedule, Course, Session
from .serializers import ProfessorSerializer, TimeSerializer, SessionSerializer, CourseSerializer
from .generator.optimizer import Optimizer

@api_view(['GET'])
def getAllProfessors(request):
    professor = Professor.objects.all()
    serializer = ProfessorSerializer(professor, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllTimes(request):
    time = Time.objects.all()
    serializer = TimeSerializer(time, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllSessions(request):
    session = Session.objects.all()
    serializer = SessionSerializer(session, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllCourses(request):
    course = Course.objects.all()
    serializer = CourseSerializer(course, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def generateSchedule(request):
    
    
    course_ids = request.GET.getlist("courses")
    semester_id = request.GET.get("semester_id")
    required_courses = request.GET.getlist("required_courses")
    blocked_times = request.GET.getlist("blocked_times")

    return Response(data)




@api_view(['POST'])
def addProfessor(request):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



