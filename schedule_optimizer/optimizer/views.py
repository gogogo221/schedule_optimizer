from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .models import Professor, Time, Schedule, Course, Session, CourseCombo
from .serializers import ProfessorSerializer, TimeSerializer, SessionSerializer, CourseSerializer, ScheduleSerializer, CourseComboSerializer, ScheduleSerializer
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
def getAllSchedules(request):
    schedule = Schedule.objects.all()
    serializer = ScheduleSerializer(schedule, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllCourseCombos(request):
    course_combo = CourseCombo.objects.all()
    serializer = CourseComboSerializer(course_combo, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAllSchedules(request):
    schedule = Schedule.objects.all()
    serializer = ScheduleSerializer(schedule, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def generateSchedule(request):
    
    
    course_ids = request.GET.getlist("courses")
    semester_id = request.GET.get("semester_id")
    required_courses = request.GET.getlist("required_courses")
    blocked_times = request.GET.getlist("blocked_times")
    want_available = request.GET.get("available")
    min_rmp = request.GET.get("min_rmp")
    max_rmp_difficulty = request.GET.get("max_rmp_difficulty")
    units_wanted = request.GET.get("units_wanted")
    optimizer = Optimizer(course_ids, 
                          semester_id, 
                          required_courses,
                          blocked_times,
                          want_available,
                          rmp=min_rmp,
                          rmp_difficulty=max_rmp_difficulty,
                          units=units_wanted)
    generated_schedules = optimizer.generate_schedules()
    filtered_combos = optimizer.filter_combinations(generated_schedules)

                          


    return Response(data)




@api_view(['POST'])
def addProfessor(request):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



