from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('search/', views.search_results, name='search_results'),
    path('cities/<int:city_id>/', views.show_city, name='show_city'),
    path('cities/<int:city_id>/add_review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/', views.show_review, name='show_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('cities/<int:review_id>/delete_review/', views.delete_review, name='delete_review'),
    path('accounts/signup/', views.signup, name='signup'),
    path('login/', views.login, {'template_name': 'login.html'}, name='login'),
]