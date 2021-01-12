from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        serializer_class = UserSerializer(self.queryset, many=True)
        return Response(serializer_class.data)