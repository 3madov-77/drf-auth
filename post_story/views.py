from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import StorySerilzed
from .models import Story
from .permissions import ReadOnly


class StoryCreate(generics.ListCreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerilzed

class StoryRetrive(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (ReadOnly,)
    queryset = Story.objects.all()
    serializer_class = StorySerilzed