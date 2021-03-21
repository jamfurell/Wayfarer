from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    name= models.CharField(max_length=100)
    current_city= models.CharField(max_length=100)
    profile_pic= models.CharField(max_length=300, null=True )
    total_reviews= models.IntegerField(null=True) 
    def set_date(self): 
        return self.user
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null =True,)
    def __str__ (self):
        return self.user.username

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class City(models.Model):
    name= models.CharField(max_length=100)
    country= models.CharField(max_length=100)
    city_pic= models.CharField(max_length=300, null=True)
    photographer= models.CharField(max_length=100, null=True)
    
    profiles = models.ManyToManyField(Profile, blank=True)
    def __str__(self):
        return self.name


class Review(models.Model):
    title= models.CharField(max_length=200)
    description= models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    
    class Meta: 
        ordering = ['-created_at']







