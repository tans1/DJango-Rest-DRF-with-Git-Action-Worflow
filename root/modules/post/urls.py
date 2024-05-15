from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CreatePost.as_view(), name='create-post'),
    path('list/', ListPosts.as_view(), name='list-posts'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update-post'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete-post'),
    path('details/<int:pk>/', PostDetails.as_view(), name='post-details'),
]
