from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('index.urls')),
    path('photos/', include('photos.urls')),
    path('videos/', include('videos.urls')),
    path('albums/', include('albums.urls')),
    path('admin/', admin.site.urls),
]