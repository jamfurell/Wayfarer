from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# Add the following import
from .forms import SignUpForm, EditProfileForm
from .models import Profile, City, Review
from django.db.models import Q




# Define the home view 
def home(request):
    return render(request, 'home.html')

def about_us(request):
    return HttpResponse('<h1>This is About Us!</h1>')

# [user: username,emailaddress, datejoined]
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    profile_user= str(profile.user)
    print(type(str(profile.user)), " <============this is the profile.user ")
    print(type(request.user.username), " <============this is the user.username ")
    print(profile.user == request.user.username)
    # print(profile.current_city, "----------------------------------------------------------------------------------")
    reviews = profile.review_set.all()
    # print(profile.user.date_joined, "<===================")
    #### NEED TO ADDRESS IF THEY DONT HAVE ANY
    # print(reviews[0].description)
    # cities= City.objects.all()
    profile_content={
        'profile': profile,
        'reviews': reviews,
        'profile_user': profile_user,
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

def search_results(request):
    query = request.GET['q']
    cities = City.objects.filter(
        Q(name__icontains=query) | Q(country__icontains=query)
    ) # new
    # print(cities, "------------------------------------------")
    return render(request, 'search_results.html', {'cities': cities})

def show_city(request, city_id):
    city = City.objects.get(id=city_id)
    # print(type(request.user.id), "<=====this is city.user")
    profile = Profile.objects.get(user=request.user)
    print(profile,"<==== this is the profile")
    
    my_reviews = profile.review_set.all()
    print(my_reviews[1].description,"<==== this is the reviews")
    city_reviews=city.review_set.all()
    print(type(city_reviews), "<===========this is all the reviews for tht city")
    show_city_content={
        'profile': profile,
        'city': city,
        'my_reviews': my_reviews,
        'city_reviews': city_reviews,
    }
    return render (request, 'city/city_detail.html', show_city_content)

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