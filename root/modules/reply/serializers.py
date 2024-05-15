from rest_framework import serializers
from .models import Reply
from modules.comment.models import Comment
from user.serializers import UserRelationshipSerializer
from modules.post.serializers import PostDetailSerializer
from modules.comment.serializers import CommentSerializer

class CreateReplySerializer(serializers.ModelSerializer):
    commentId = serializers.IntegerField()
    
    class Meta:
        model = Reply
        fields = ['content','commentId']
    
    def validate(self, data):
        if not data['content']:
            raise serializers.ValidationError("Content of reply is required")
        if not (comment := Comment.objects.filter(id=data['commentId'])).exists():
            raise serializers.ValidationError("Comment to be replied is not found")
        
        return data
        
    def create(self, validated_data):
        commentId = validated_data.pop('commentId')
        comment = Comment.objects.get(id = commentId)
        
        # validated_data['comment'] = comment
        # validated_data['post'] = comment.post
        reply = Reply.objects.create(comment=comment , post=comment.post, **validated_data)
        # reply = Reply.objects.create(p)
        
        return reply
        
    
    

class UpdateReplySerializer(serializers.ModelSerializer):
    pass

class DetailReplySerializer(serializers.ModelSerializer):
    author = UserRelationshipSerializer()
    post = PostDetailSerializer()
    comment = CommentSerializer()
    
    class Meta:
        model = Reply
        fields = '__all__'
        # [
        #     'id',
        #     'content',
        #     'date_replied',
        #     'author',
        #     'post',
        #     'comment'
        # ]

