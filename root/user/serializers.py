from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name','last_name','is_staff', 'is_active', 'date_joined')
        read_only_fields = ('id', 'is_staff', 'is_active', 'date_joined')

class UserRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name','last_name')

class RegisterUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','confirm_password','first_name','last_name')
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        if not data['username']:
            raise serializers.ValidationError({'username': 'Username is required.'})
        if not data['password']:
            raise serializers.ValidationError({'password': 'Password is required.'})
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': 'User not found.'})
        if (not (user := User.objects.get(username=data['username'])).check_password(data['password'])):
            raise serializers.ValidationError({'password': 'Incorrect password.'})

        return data



