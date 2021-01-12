from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post"]