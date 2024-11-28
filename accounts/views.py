from django.shortcuts import render

# Create your views here.
"""The views.py file in the accounts app contains the views for the different account-related pages such as login, signup,
 forgot password, change password, dashboard, and profile.
 Each view function renders a corresponding HTML template file located in the accounts/templates/accounts directory."""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User


"""The login_view function handles the login logic, the signup_view function handles the signup logic, the forgot_password_view."""
@login_required
def login_view(request):
    # Handle login logic
    return render(request, 'accounts/login.html')

"""The signup_view function handles the signup logic, the forgot_password_view function handles the password reset email sending logic."""
@login_required
def signup_view(request):
    # Handle signup logic
    return render(request, 'accounts/signup.html')

"""The forgot_password_view function handles the password reset email sending logic, the change_password_view function allows users to change passwords."""
@login_required
def forgot_password_view(request):
    # Handle password reset email sending
    return render(request, 'accounts/forgot_password.html')

"""The change_password_view function allows users to change passwords, the dashboard_view function renders the dashboard with user info."""
@login_required
def change_password_view(request):
    # Allow users to change passwords
    return render(request, 'accounts/change_password.html')

"""The dashboard_view function renders the dashboard with user info, the profile_view function renders the profile page with user details."""
@login_required
def dashboard_view(request):
    # Dashboard with user info
    return render(request, 'accounts/dashboard.html')

"""The profile_view function renders the profile page with user details."""
@login_required
def profile_view(request):
    # Profile page with user details
    return render(request, 'accounts/profile.html')
