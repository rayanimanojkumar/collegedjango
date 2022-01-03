# from django.shortcuts import render
from rest_framework import viewsets

from .models import StudentDetails, Course, Subjects, Teachers, Marks
from .serializers import StudentDetailsSerializers,CourseSerializers,SubjectsSerializers,TeachersSerializers,MarksSerializers

class StudentDetailsViewSet(viewsets.ModelViewSet):
    queryset= StudentDetails.objects.all()
    serializer_class = StudentDetailsSerializers

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

class SubjectsViewSet(viewsets.ModelViewSet):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializers

class TeachersViewSet(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializers

class MarksViewSet(viewsets.ModelViewSet):
    queryset = Marks.objects.all()
    serializer_class = MarksSerializers