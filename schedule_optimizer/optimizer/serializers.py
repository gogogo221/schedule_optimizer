from rest_framework import serializers
from .models import Professor, Time, Schedule, Course, Session, CourseCombo
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
    sessions = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="id"
    )    
    class Meta:
        model = Course
        fields = "__all__"

class CourseComboSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    sessions = SessionSerializer(many=True)
    times = TimeSerializer(many=True)
    class Meta:
        model = CourseCombo
        fields = ["id", "course", "sessions", "times"]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]
class ScheduleSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    course_combos = CourseComboSerializer(many=True)

    class Meta:
        model = Schedule
        fields = "__all__"

    def create(self, validated_data):
        course_combos = validated_data.pop("course_combos")
        
