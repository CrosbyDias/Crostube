from django.urls import path
from .views import *


urlpatterns = [
    path('home/', home, name='home'),
    path('upload_video/', upload_video, name='upload_video'),
    path('video/<int:video_id>/', video_detail, name='video_detail'),
]