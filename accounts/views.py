from .serializers import UserSerializer
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

# Create your views here.


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    
