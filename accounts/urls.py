from django.urls import path
from . import views

"""The URL configuration for the accounts app. This file is used to define the URL patterns for the views in the accounts app. 
The views are imported from the views.py file in the accounts app. The urlpatterns list routes URLs to views. The path() function is used to define the URL patterns. The first argument is the URL pattern, the second argument is the view function, and the third argument is the name of the URL pattern. The name of the URL pattern is used to refer to the URL pattern in templates and other parts of the Django project."""
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
]
