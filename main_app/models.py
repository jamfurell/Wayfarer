from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    current_city= models.CharField(max_length=100)
    profile_pic= models.CharField(max_length=300, null=True )
    total_reviews= models.IntegerField(null=True) 

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
    
    profiles = models.ManyToManyField(Profile, blank=True)
    def __str__(self):
        return self.name


class Review(models.Model):
    description= models.CharField(max_length=1000)
    title= models.CharField(max_length=200)

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


    ## testing manually providing city info
    # class City:
    #     def __init__(self, name, country, city_pic):
    #         self.name= name
    #         self.country= country
    #         self.city_pic= city_pic

    # City=[
    #     City("Milano", "Italy", "https://thumbs.dreamstime.com/t/milan-italy-145861739.jpg"),
    #     City("Los Angeles", "USA", "https://media.istockphoto.com/photos/hollywood-sign-from-central-picture-id1126093641?k=6&m=1126093641&s=612x612&w=0&h=jIVY1Ow3swxS5h0vUslvxkFKllpVLR07i_HbKKSSn-0="),
    # ]
