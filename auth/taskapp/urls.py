from django.urls import path
from .views import *

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('my-task/<str:pk>/',showParticularTask,name='my-task'),
    path('showAllTask/',showAllTask,name='showAllTask'),
    path('del-task/<str:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    
]