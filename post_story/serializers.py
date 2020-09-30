from .models import Story
from rest_framework import serializers

class StorySerilzed(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('auther', 'title', 'body', 'created_at',)