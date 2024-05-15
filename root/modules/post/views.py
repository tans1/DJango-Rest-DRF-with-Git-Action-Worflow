from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status


class CreatePost(CreateAPIView):
    serializer_class = CreatePost
    
    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()
        return super().perform_create(serializer)
    
class ListPosts(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPosts
    
class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        post = self.get_object()
        if (user := self.request.user) != post.author:
            raise PermissionDenied('You do not have permission to perform this action.')
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Post deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)

class UpdatePost(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = UpdatePost
    
    def update(self, request, *args, **kwargs):
        post = self.get_object()
        if (user := self.request.user) != post.author:
            raise PermissionDenied('You do not have permission to perform this action.')
        return super().update(request, *args, **kwargs)
    
class PostDetails(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ListPosts