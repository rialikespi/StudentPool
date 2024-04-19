from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfilePicture
from django.contrib import messages
import re

# Create your views here.
def home(request) :
    return HttpResponse()

@login_required(login_url="")
def profile(request):

    current_user = request.user
    user = Profile.objects.get(user = current_user)
    
    context = {"user" : user}

    return render (request, "profile.html", context)


@login_required(login_url="")
def settingsPage(request) :
    
    current_user = request.user
    user = Profile.objects.get(user = current_user)
    form = ProfilePicture(instance=user)

   
    if request.method == "POST":

        form = ProfilePicture(request.POST, request.FILES, instance=user)
        
        if form.is_valid():
            form.save(commit=True)
        

        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        valid = False
 

        #name
        first_name = request.POST.get('f_name')
        last_name = request.POST.get('l_name')

        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        
        user.save()

        #email
        new_email = request.POST.get('email')

        valid = (re.fullmatch(regex, new_email))

        

        #CHANGE USER EMAIL

        if new_email and valid:
            user.user.email = new_email
            user.save()
        else:
            return redirect('/settings')
        user.save()
    
    context = {"form" : form, "user" : user}

    return render(request, "settings.html", context)