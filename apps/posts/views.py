from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PostsSerializer
from .models import Posts

# class PostsViewSet(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer
#     http_method_names = ["get", "post"]

class PostsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Posts.objects.all()
        serializer = PostsSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Posts.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostsSerializer(post)

        return Response(serializer.data)