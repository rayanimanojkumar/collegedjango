from rest_framework import serializers
from .models import StudentDetails, Course, Subjects, Teachers, Marks

class StudentDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentDetails
        fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):
     class Meta:
         model = Course
         fields = '__all__'

class SubjectsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'

class TeachersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'

class MarksSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'
