from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='all-task'),
    path('tasks/<str:pk>/',TaskView.as_view(),name='my-task'),
    path('tasks/',TaskView.as_view(),name='create-task'),
    path('tasks/<str:pk>/', TaskView.as_view(), name='task-delete'),
    path('tasks/<str:pk>/', TaskView.as_view(), name='task-update'),
    
]