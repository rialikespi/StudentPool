from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"), #<- root url, render HTTP-Response
    path("profile/", views.profile, name="profile"), #<- main profile
    path("settings/", views.settingsPage, name="user settings"), #<- profile settings
]