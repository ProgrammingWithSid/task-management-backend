from django.urls import path,include
from .views import *


urlpatterns = [

    path('profile/',getUserProfile,name="user_profile"),
    path('profile/update/',updateUserProfile,name="user_profile_update"),

]

