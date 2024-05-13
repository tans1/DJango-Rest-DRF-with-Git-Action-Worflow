from rest_framework import serializers
from .models import Comment
from modules.post.models import Post
from user.serializers import UserRelationshipSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserRelationshipSerializer()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'date_commented',
            'author',
        ]

class CreateComment(serializers.ModelSerializer):
    postId = serializers.IntegerField()
    
    class Meta:
        model = Comment
        fields = ['content','postId']
    
    def create(self, validated_data):
        post_id = validated_data.pop('postId')
        post = Post.objects.get(id=post_id)
        comment = Comment.objects.create(post=post, **validated_data)
        return comment

class ListComments(serializers.ModelSerializer):
    author = UserRelationshipSerializer()
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'date_commented',
            'author',
        ]

class UpdateComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content']
    
    def validate(self, data):
        if not data['content']:
            raise serializers.ValidationError({'content': 'Content is required.'})
        
        return data
    
    def update(self, instance, validated_data):
        if not Comment.objects.filter(id=instance.id).exists():
            raise serializers.ValidationError({'message': 'Comment not found.'})
        
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
    