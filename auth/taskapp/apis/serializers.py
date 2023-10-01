from rest_framework import serializers
from taskapp.models import *
from users.serializers import CustomUserCreateSerializer

class TaskAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskApp
        fields = ['uuid','taskName','description']


