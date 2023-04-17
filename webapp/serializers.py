from rest_framework import serializers
from .models import employees
from . models import client
from rest_framework import serializers
from .models import Project

class employeesSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        #fields=('firstname','lastname')
        fields='__all__'

class clientSerializer(serializers.ModelSerializer):
    class Meta:
        model = client
        fields = ('id', 'client_name', 'created_at', 'created_by')
        read_only_fields = ('id', 'created_at', 'created_by')



class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']
# Create your models here.