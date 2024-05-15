from django.db import models
from user.models import User
from modules.post.models import Post

class Comment(models.Model):
    content = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    
    def __str__(self):
        return self.content