from django.utils.timezone import now
import logging
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

logger = logging.getLogger(__name__)

def home_views(request):
    return render(request, 'accounts/home.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login in successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'accounts/login.html')
    else:
        form = AuthenticationForm()
        messages.error(request, 'Method failed')
    return render(request, 'accounts/login.html', {'form': form})
