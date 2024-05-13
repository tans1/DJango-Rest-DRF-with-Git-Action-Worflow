from django.db import models
from user.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

   