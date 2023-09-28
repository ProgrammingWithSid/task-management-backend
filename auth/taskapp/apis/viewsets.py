from rest_framework import viewsets
from taskapp.models import *
from taskapp.apis.serializers import *
from rest_framework.permissions import IsAuthenticated

class TaskAppViewsets(viewsets.ModelViewSet):
    queryset = TaskApp.objects.all()
    serializer_class = TaskApp
    permission_classes = [IsAuthenticated]