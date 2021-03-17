from django import forms
from .models import City, Review, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # first_name= forms.TextInput(max_length=100)
    # last_name= forms.TextInput(max_length=100)
    current_city = forms.CharField(max_length=100)
    class Meta: 
        model = User
        fields = ['username', 'email', 'first_name', 'current_city']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'current_city', 'profile_pic']