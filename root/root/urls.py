from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('user/', include('user.urls')),
    
    path('comment/', include('modules.comment.urls')),
    path('post/', include('modules.post.urls')),
    path('reply/', include('modules.reply.urls')),
]
