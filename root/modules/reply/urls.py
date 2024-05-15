from django.urls import path
from .views import CreateReply, DetailViewReply

urlpatterns = [
    path('create/', CreateReply.as_view(), name="create a reply"),
    path('details/<int:pk>/', DetailViewReply.as_view(), name="detail of a reply")
]
