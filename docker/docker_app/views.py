from django.shortcuts import render
from .serializers import TeacherSerializer, StudentSerializer
from .models import Teacher, Student 
from rest_framework import viewsets 

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer 

class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 


