from rest_framework import serializers 
from docker_app.models import Student, Teacher  

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher 
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = '__all__'

        