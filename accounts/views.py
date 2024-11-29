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

def home_view(request):
    return render(request, 'accounts/home.html')

"""The login_view function handles the login logic, the signup_view function handles the signup logic, the forgot_password_view."""
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')


"""The signup_view function handles the signup logic."""
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


"""The forgot_password_view function handles the password reset email sending logic, the change_password_view function allows users to change passwords."""
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
