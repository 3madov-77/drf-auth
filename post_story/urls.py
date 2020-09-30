from django.urls import path, include
from .views import StoryCreate, StoryRetrive

urlpatterns = [
    path('', StoryCreate.as_view(), name='all_stories'),
    path('<int:pk>', StoryRetrive.as_view(), name='story_details'),
]