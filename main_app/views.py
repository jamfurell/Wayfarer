from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, EditProfileForm, AddReviewForm
from .models import Profile, City, Review
# for filtering city search results
from django.db.models import Q




# Define the home view 
def home(request):
    cities = City.objects.all()
    signup_form = SignUpForm()
    login_form = AuthenticationForm()
    return render(request, 'home.html', {'signup_form':signup_form, 'login_form':login_form, 'cities':cities})

# Define the about us view 
def about_us(request):
    return render(request, 'aboutus.html')

# Define the user profile view 
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    profile_user= str(profile.user)
    reviews = profile.review_set.all()
    profile_content={
        'profile': profile,
        'reviews': reviews,
        'profile_user': profile_user,
    }
    return render(request, 'profile/profile.html', profile_content)

# Define the edit user profile view 
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

# Define the show review view 
def show_review(request, review_id):
    review = Review.objects.get(id=review_id)
    editreview_form= AddReviewForm()
    return render(request, 'review/detail.html', {'review': review, 'editreview_form':editreview_form})

# Define the edit review view 
@login_required
def edit_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if review.profile == request.user.profile:
        ## HANDLE IF THEY EDIT A POST THAT THEY DONT OWN
        if request.method == 'POST':
            form = AddReviewForm(request.POST, instance = review)
            if form.is_valid():
                form.save()
                return redirect('show_review', review_id)
        else:
            form = AddReviewForm(instance = review)
            context = {
                "review_id": review_id,
                "form": form,
            }
            return render(request, "review/edit_review.html", context)

# Define the search city results view 
def search_results(request):
    query = request.GET['q']
    cities = City.objects.filter(
        Q(name__icontains=query) | Q(country__icontains=query)
    )
    return render(request, 'search_results.html', {'cities': cities})

# Define the show city detail view 
def show_city(request, city_id):
    city = City.objects.get(id=city_id)
    profile = Profile.objects.get(user=request.user)
    my_reviews = profile.review_set.all()
    city_reviews=city.review_set.all()
    show_city_content={
        'profile': profile,
        'city': city,
        'my_reviews': my_reviews,
        'city_reviews': city_reviews,
    }
    return render (request, 'city/city_detail.html', show_city_content)

# Define the add review view 
def add_review(request, city_id):
    profile = Profile.objects.get(user=request.user)
    city = City.objects.get(id=city_id)
    form = AddReviewForm(request.POST or None)
    if request.POST and form.is_valid():
        new_review = form.save(commit=False)
        new_review.city = city
        new_review.profile= profile
        new_review.save()
        return redirect('show_city', city_id= city_id)
    else:
        return render(request, 'city/city_detail.html', {"form": form, 'city_id':city_id})

# Define the delete review view 
@login_required
def  delete_review (request, review_id):
    thereview= Review.objects.get(id=review_id)
    city_id= thereview.city.id
    Review.objects.get(id=review_id).delete()
    return redirect ('show_city', city_id=city_id)

# Define the signup form view 
def signup(request):
    error_message= ''
    if request.method == 'POST': 
        print("You are in the POST signup function!")
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
    print("You failed getting the signup function--this is the =====>", request, "<=======")
    return redirect('home')

# Define the login form view 
def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile', login)
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})