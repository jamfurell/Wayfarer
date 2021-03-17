from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('review/<int:review_id>/', views.show_review, name='show_review'),
    path('accounts/signup/', views.signup, name='signup'),
]