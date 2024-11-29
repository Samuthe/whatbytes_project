from datetime import timedelta, datetime
import logging
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from django.core.cache import cache
import os
from django.utils import timezone
from .models import CustomUser

logger = logging.getLogger(__name__)

MAX_OTP_REQUESTS = 5
OTP_REQUEST_TIME_WINDOW = 3600 

def home_views(request):
    return render(request, 'accounts/home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        remember = request.POST.get("remember")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            expiry_time = timezone.now() + timedelta(minutes=30)
            if remember is not None:
                otp = get_random_string(length=6, allowed_chars='0123456789')
                request.session['otp'] = otp
                request.session['username'] = username
                send_mail(
                    'Your OTP Code',
                    f'Your OTP for login is {otp}\n\nPlease enter this code to complete the login.\nexpiry time: 30 minutes\n\nThank you.\nWhatbytes',
                    os.getenv('EMAIL_HOST_USER'),
                    [user.email],
                    fail_silently=False,
                )
                request.session['expiry_time'] = expiry_time.isoformat()
                request.session['password'] = password 
                request.session.modified = True
                return redirect('verify_otp')
            login(request, user)
            request.session['expiry_time'] = expiry_time.isoformat()
            request.session.modified = True
            messages.success(request, 'Login in successful', extra_tags='success')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'accounts/login.html')
    else:
        form = AuthenticationForm()
        messages.error(request, 'Method failed', extra_tags='error')
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            print(f"Email from form: {email}")

            email_check = CustomUser.objects.filter(email=email)
            print(f"Email check result: {email_check}")
            
            if email_check.exists():
                form.add_error('email', 'Email already exists.')
                return render(request, 'accounts/register.html', {'form': form})
            form.save()
            messages.success(request, 'Account created successfully.', extra_tags='success')
            send_mail(
                'Account Created Successfully.',
                'Congratulation!!! Your account has been created.\n\nThank you.\nWhatbytes',
                os.getenv('EMAIL_HOST_USER'),
                [form.instance.email],
                fail_silently=False,
            )
            otp = get_random_string(length=6, allowed_chars='0123456789')
            request.session['otp'] = otp
            request.session['username'] = form.instance.username
            send_mail(
                'Registration Confirmation Code',
                f'Your OTP for registration is: {otp}\n\nPlease enter this code to complete the registration.\n\nThank you.\nWhatbytes',
                os.getenv('EMAIL_HOST_USER'),
                [form.instance.email],
                fail_silently=False,
            )
            request.session['password'] = password
            return redirect('verify_otp')
    else:
        form = CustomUserCreationForm()
        messages.error(request, 'Registration failed', extra_tags='error')
    return render(request, 'accounts/register.html', {'form': form})

def generate_otp(request):
    if request.method == "POST":
        username = request.POST["username"]
        
        user = authenticate(request, username=username)
        
        if user:
            otp_key = f"otp_requests_{username}"
            otp_data = cache.get(otp_key, {'count': 0, 'timestamp': timezone.now()})

            last_request_time = datetime.fromisoformat(otp_data['timestamp'])
            time_since_last_request = (timezone.now() - last_request_time).total_seconds()

            if time_since_last_request > OTP_REQUEST_TIME_WINDOW:
                otp_data['count'] = 0
                otp_data['timestamp'] = timezone.now()

            if otp_data['count'] >= MAX_OTP_REQUESTS:
                messages.error(request, 'You have reached the maximum number of OTP requests. Please try again later.')
                return render(request, 'accounts/generate_otp.html')

            otp_data['count'] += 1
            cache.set(otp_key, otp_data, timeout=OTP_REQUEST_TIME_WINDOW)

            otp = get_random_string(length=6, allowed_chars='0123456789')
            
            expiration_time = timezone.now() + timedelta(minutes=30)
            request.session['otp'] = otp
            request.session['username'] = username
            request.session['otp_expiry'] = expiration_time.isoformat()
            
            send_mail(
                'Your OTP Code',
                f'Your OTP code is: {otp}',
                os.getenv('EMAIL_HOST_USER'),
                [user.email],
                fail_silently=False,
            )
            
            messages.info(request, 'OTP has been sent to your email address.')
            return redirect('verify_otp')
        else:
            messages.error(request, 'Invalid username or user does not exist.')

    return render(request, 'accounts/generate_otp.html')

def verify_otp(request):
    if request.method == "POST":
        otp = str(request.POST.get("otp", "").strip())
        session_otp = request.session.get('otp')
        username = request.session.get('username')
        password = request.session.get('password')

        if not session_otp or not username:
            messages.error(request, 'Session data is missing or expired.')
            return redirect('login')        
        
        if otp == session_otp:
            user = authenticate(username=username, password=password)
            print(f"User: {user} Username: {username} Password: {password}")
            if user:
                login(request, user)
                if request.session.get('remember'):
                    expiry_time = timezone.now() + timedelta(weeks=1)
                    request.session['expiry_time'] = expiry_time.isoformat()
                    request.session.modified = True
                else:
                    request.session.set_expiry(0)
                messages.success(request, 'Login successful.')
                expiry_time = timezone.now() + timedelta(minutes=30)
                request.session['expiry_time'] = expiry_time.isoformat()
                request.session['password'] = '' # Clear password from session
                request.session.modified = True
                return redirect('dashboard')
            else:
                messages.error(request, 'Authentication failed.')
        else:
            messages.error(request, 'Invalid OTP.')

    return render(request, 'accounts/verify_otp.html')

@login_required
def dashboard_views(request):
    return render(request, 'accounts/dashboard.html')

@login_required
@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.', extra_tags='success')
    return redirect('login')