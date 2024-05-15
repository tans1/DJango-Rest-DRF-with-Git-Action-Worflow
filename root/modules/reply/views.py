from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .serializers import *

class CreateReply(CreateAPIView):
    serializer_class = CreateReplySerializer
    
    def perform_create(self, serializer):
        serializer.validated_data['author'] = self.request.user
        serializer.save()
        
        return super().perform_create(serializer)

class DetailViewReply(RetrieveAPIView):
    serializer_class =  DetailReplySerializer

    def get_queryset(self):
        return Reply.objects.all()
    
