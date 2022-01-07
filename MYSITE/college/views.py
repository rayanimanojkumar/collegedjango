# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

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
    
class MarksView(generics.ListAPIView):
    queryset = Marks.objects.raw('SELECT t1.student_id, t1.subject_id,  t1.sem_marks, t1.id, t1.internal_marks, total_marks FROM collegedetails.college_marks t1 JOIN ( SELECT MAX(t2.total_marks) total_marks FROM collegedetails.college_marks t2 ) t3 USING (total_marks);')

    serializer_class = MarksSerializers

class  StudentView(generics.ListAPIView):
    queryset = StudentDetails.objects.raw('SELECT * FROM collegedetails.college_studentdetails LIMIT 3;')
    serializer_class = StudentDetailsSerializers    
 
