from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreateComment.as_view(), name='create_comment'),
    path('list/postId=<int:postId>/', ListComments.as_view(), name='list_comments'),
    path('update/<int:pk>/', UpdateComment.as_view(), name='update_comment'),
    path('delete/<int:pk>/', DeleteComment.as_view(), name='delete_comment'),
]
