from rest_framework import serializers
from .models import Professor, Schedule
from django.contrib.auth.models import User


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]
class ScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Schedule
        fields = "__all__"
    


