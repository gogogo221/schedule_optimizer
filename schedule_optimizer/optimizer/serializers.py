from rest_framework import serializers
from .models import Professor, Time, Schedule, Course, Session
from django.contrib.auth.models import User


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"

class SessionSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    time = TimeSerializer()
    class Meta:
        model = Session
        fields = "__all__"

class CourseSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)
    
    class Meta:
        model = Course
        fields = ["name", "tag", "units", "schedule", "semester", "sessions"]

