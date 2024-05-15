from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class RegisterUser(CreateAPIView):
    authentication_classes = [] # No authentication required for registration
    serializer_class = RegisterUserSerializer
    def perform_create(self, serializer):
        return super().perform_create(serializer)
    

class LoginUser(APIView):
    authentication_classes = [] # No authentication required for login
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data['username'])
        token = AccessToken.for_user(user)
        return Response({'token': str(token)})

class UserDetails(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'
    
    def get_object(self):
        user = self.request.user
        return user