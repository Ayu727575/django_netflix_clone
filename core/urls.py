from .views import Home, ProfileList
from django.urls import path

app_name='core'

urlpatterns = [
    path('',Home.as_view()),
    path('profile/',ProfileList.as_view(), name='profile_list')
]

