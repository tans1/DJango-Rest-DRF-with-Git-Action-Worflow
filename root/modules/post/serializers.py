from rest_framework import serializers
from .models import Post
from modules.comment.serializers import *
from user.serializers import UserRelationshipSerializer

class CreatePost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']

class ListPosts(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = UserRelationshipSerializer()
    class Meta:
        model = Post
        fields = ["id", "title","body","date_posted","author", "comments"]

class UpdatePost(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'body']
    
    def validate(self, data):
        if not data['title']:
            raise serializers.ValidationError({'title': 'Title is required.'})
        if not data['body']:
            raise serializers.ValidationError({'body': 'Body is required.'})
        
        return data
    
    def update(self, instance, validated_data):
        if not Post.objects.filter(id=instance.id).exists():
            raise serializers.ValidationError({'message': 'Post not found.'})
        
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance

class PostDetailSerializer(serializers.ModelSerializer):
    author = UserRelationshipSerializer()
    class Meta:
        model = Post
        fields = ["id", "title","body","date_posted","author"]