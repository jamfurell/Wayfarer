from django import forms
from .models import City, Review, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    current_city = forms.CharField(max_length=100)
    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'current_city']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city', 'profile_pic']

class AddReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=200, required=True)
    description = forms.CharField(max_length=1000, required=True)
    class Meta:
        model = Review
        fields = ['title', 'description']