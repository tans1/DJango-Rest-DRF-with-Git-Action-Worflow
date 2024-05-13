from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework import status

class CreateComment(CreateAPIView):
    serializer_class = CreateComment
    
    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()
        return super().perform_create(serializer)
    
class ListComments(ListAPIView):
    serializer_class = ListComments
    
    def get_queryset(self):
        postId = self.kwargs.get('postId')
        
        queryset = Comment.objects.filter(post_id=postId)
        
        return queryset

class UpdateComment(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = UpdateComment
    
    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        if (user := self.request.user) != comment.author:
            raise PermissionDenied('You do not have permission to perform this action.')
        return super().update(request, *args, **kwargs)

class DeleteComment(DestroyAPIView):
    queryset = Comment.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()
        if (user := self.request.user) != comment.author:
            raise PermissionDenied('You do not have permission to perform this action.')
        super().destroy(request, *args, **kwargs)
        return Response({'message': 'Comment deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)