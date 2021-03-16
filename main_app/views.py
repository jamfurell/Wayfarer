from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Add the following import
from .forms import SignUpForm
from .models import Profile, City, Review




# Define the home view 
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return HttpResponse('<h1>This is About Us!</h1>')

def profile(request):
    cities= City.objects.all()
    return render(request, 'profile/profile.html', {'cities': cities})

def signup(request):
    error_message= ''
    if request.method == 'POST': 
        ##how we create a user form object that include data from browser
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('index')
        else: 
            print(form.errors.as_json())
            error_message = 'Invalid sign up - try again'
    form= SignUpForm()
    context= {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)