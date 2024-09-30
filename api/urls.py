from django.urls import path
from .views import get_subtitles

urlpatterns = [
    path('get_subtitles/', get_subtitles),
]
