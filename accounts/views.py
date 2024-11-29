from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

def login_view(request):
    # Handle login logic
    return render(request, 'accounts/templates/accounts/login.html')

def signup_view(request):
    # Handle signup logic
    return render(request, 'accounts/templates/accounts/signup.html')

def forgot_password_view(request):
    # Handle password reset email sending
    return render(request, 'accounts/templates/accounts/forgot_password.html')

@login_required
def change_password_view(request):
    # Allow users to change passwords
    return render(request, 'accounts/templates/accounts/change_password.html')

@login_required
def dashboard_view(request):
    # Dashboard with user info
    return render(request, 'accounts/templates/accounts/dashboard.html')

@login_required
def profile_view(request):
    # Profile page with user details
    return render(request, 'accounts/templates/accounts/profile.html')
