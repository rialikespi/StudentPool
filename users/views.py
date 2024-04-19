from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required
def index(request):
   
   return render(request, "index.html",{})


def signup_user(request):
    context = {}
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save(commit = True)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, 'Account was created for ' + username)
            return redirect("/signin/")
        else:
            # Handle the case where form validation fails
            messages.error(request, 'Please correct the errors below.')

    context.update({
       "form": form,
       "title": "Sign up",
    })

    return render(request, "signup.html", context)

def signin_user(request):

    context = {}
    form = AuthenticationForm(request, data=request.POST)

    if request.method == 'POST':
       if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)  
           return redirect("/index/")  
        else:
           messages.success(request, "There was an Error Signing In, Please Try Again")
           return redirect('/signin')
    
    context.update({
       "form" : form, 
       "title": "Signin",
    })

    return render(request, "signin.html", context)

def logout_user(request):
   logout(request)
   messages.success(request,("You Were Successfully Logged Out"))
   return redirect(reverse('signin'))
   
