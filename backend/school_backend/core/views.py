from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'})
    return Response(serializer.errors)