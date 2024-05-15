from django.db import models
from user.models import User
from modules.post.models import Post
from modules.comment.models import Comment

class Reply(models.Model):
    content = models.TextField()
    date_replied = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="reply")
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="reply")
    comment = models.ForeignKey(to=Comment, on_delete=models.CASCADE, related_name="reply")
    
    
    def __str__(self) -> str:
        return self.content