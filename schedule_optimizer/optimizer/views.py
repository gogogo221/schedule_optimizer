from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .models import Professor, Schedule
from .serializers import ProfessorSerializer, ScheduleSerializer
from .generator.optimizer import Optimizer
import json
from .generator.serializers import ComplexEncoder
from rest_framework import status
from rest_framework import generics, permissions


@api_view(['GET'])
def getAllProfessors(request):
    professor = Professor.objects.all()
    serializer = ProfessorSerializer(professor, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getAllSchedules(request):
    schedule = Schedule.objects.all()
    serializer = ScheduleSerializer(schedule, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getSchedules(request):
    user = User.objects.get(id=request.user.id)
    schedules = Schedule.objects.filter(user=user)
    print(schedules)
    serializer = ScheduleSerializer(schedules, many=True)
    return Response(data={"user":request.user.id, "schedules":serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def generateSchedule(request):

    course_ids = request.GET.getlist("courses")
    semester_id = request.GET.get("semester_id")
    required_courses = request.GET.getlist("required_courses")
    blocked_times = request.GET.getlist("blocked_times")
    want_available = request.GET.get("available")
    min_rmp = request.GET.get("min_rmp")
    min_rmp = float(min_rmp) if min_rmp else None
    max_rmp_difficulty = request.GET.get("max_rmp_difficulty")
    max_rmp_difficulty = float(max_rmp_difficulty) if max_rmp_difficulty else None
    units_wanted = request.GET.get("units_wanted")
    units_wanted = int(units_wanted) if units_wanted else None
    optimizer = Optimizer(course_ids, 
                          semester_id, 
                          required_courses,
                          blocked_times,
                          want_available,
                          rmp=min_rmp,
                          rmp_difficulty=max_rmp_difficulty,
                          units=units_wanted)
    generated_schedules = optimizer.generate_schedules()
    filtered_schedules = optimizer.filter_combinations(generated_schedules)
    #need to serialize filtered_combos 
    data = json.dumps(filtered_schedules, cls=ComplexEncoder)

    return Response(data)




@api_view(['POST'])
def addProfessor(request):
    serializer = ProfessorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["GET"])
def isLoggedIn(request):
    if request.user.is_authenticated:
        return Response( status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def addSchedule(request):
    if request.user.is_authenticated:
        serializer = ScheduleSerializer(data=request.data)
        #get the user and set in the serializer
        if serializer.is_valid():
            #serializer.user = User.objects.get(id=request.user.id) 
            serializer.save(user=User.objects.get(id=request.user.id))
            #schedule_instance.user
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #if valid; save
        #return response
    return Response("user not logged in", status=status.HTTP_401_UNAUTHORIZED)

