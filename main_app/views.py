from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Add the following import
from .forms import SignUpForm, EditProfileForm
from .models import Profile, City, Review




# Define the home view 
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return HttpResponse('<h1>This is About Us!</h1>')

# [user: username,emailaddress, datejoined]
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    # print(profile.current_city, "----------------------------------------------------------------------------------")
    reviews = profile.review_set.all()
    print(profile.user.date_joined, "<===================")
    #### NEED TO ADDRESS IF THEY DONT HAVE ANY
    # print(reviews[0].description)
    # cities= City.objects.all()
    profile_content={
        'profile': profile,
        'reviews': reviews,
    }
    return render(request, 'profile/profile.html', profile_content)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance = profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance = profile)
        return render(request, 'profile/edit_profile.html', {'form' : form})

def show_review(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'review/detail.html', {'review': review})

def signup(request):
    error_message= ''
    if request.method == 'POST': 
        ##how we create a user form object that include data from browser
        form = SignUpForm(request.POST)
        if form.is_valid():
            user= form.save()
            # load the profile instance created by the signal
            user.refresh_from_db()  
            user.profile.current_city = form.cleaned_data.get('current_city')
            user.save()
            login(request,user)
            return redirect('profile')
        else: 
            print(form.errors.as_json())
            error_message = 'Invalid sign up - try again'
    form= SignUpForm()
    context= {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)