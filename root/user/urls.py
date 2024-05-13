from django.urls import path
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('details/', UserDetails.as_view(), name='user-details'),
]
