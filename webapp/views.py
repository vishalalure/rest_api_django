from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer 
from rest_framework import generics
from django.views.generic import DetailView #temp
from .models import client
from .serializers import clientSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Client
from .serializers import ProjectSerializer


class employeeList(APIView):

    def get(self,request):
        employees1=employees.objects.all()
        serializer=employeesSerializer(employees1,many=True)
        return Response(serializer.data)
    
    def post(self):
        pass


class clientCreateView(generics.CreateAPIView):
    queryset = client.objects.all()
    serializer_class = clientSerializer 
    
    
    #temp
def get_client_with_projects(request, client_id):
    client = get_object_or_404(client, pk=client_id)
    projects = client.project_set.all()

    response_data = {
        'id': client.id,
        'client_name': client.client_name,
        'projects': [{'id': p.id, 'name': p.name} for p in projects],
        'created_at': client.created_at,
        'created_by': client.created_by,
        'updated_at': client.updated_at,
    }

    return JsonResponse(response_data)



def update_client(request, id):
    try:
        client = client.objects.get(id=id)
    except client.DoesNotExist:
        return JsonResponse({'error': 'Client not found'}, status=404)
    
    if request.method == 'PUT':
        # Update all fields
        client.client_name = request.POST.get('client_name')
        # ... add more fields here if needed
        
    elif request.method == 'PATCH':
        # Update only the provided fields
        for field, value in request.POST.items():
            if field == 'client_name':
                client.client_name = value
            # ... add more fields here if needed
            
    client.save()
    
    return JsonResponse({
        'id': client.id,
        'client_name': client.client_name,
        'created_at': client.created_at,
        'created_by': client.created_by,
        'updated_at': client.updated_at,
    })

#temp
@api_view(['POST'])
def create_project(request, id):
    client = get_object_or_404(Client, pk=id)

    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        project = serializer.save(client=client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

