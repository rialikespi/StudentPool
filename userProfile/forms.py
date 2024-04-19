from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import *

class ProfilePicture(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_picture',)