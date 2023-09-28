from django.shortcuts import render
from .models import *
from .apis.serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def showAllTask(request):
    user = request.user

    selected_user = TaskApp.objects.filter(user=user)

    serializer = TaskAppSerializer(selected_user,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def showParticularTask(request,pk):
    user = request.user

    task = get_object_or_404(TaskApp,uuid=pk)

    selected_user = TaskApp.objects.filter(user=user,uuid=task)

    serializer = TaskAppSerializer(selected_user)

    return Response(serializer.data)


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskAppSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDeleteView(APIView):

    def delete(self,request,pk):
        user = request.user
        try:
            task = TaskApp.objects.get(user=user,uuid=pk)
        except TaskApp.DoesNotExist:
            return Response({'error : Task Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
