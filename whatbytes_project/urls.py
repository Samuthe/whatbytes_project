"""
URL configuration for whatbytes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render
    
    
"""The URL configuration for the whatbytes_project project. This file is used to define the URL patterns for the views in the project. 
The views are imported from the views.py file in the project. The urlpatterns list routes URLs to views. 
The path() function is used to define the URL patterns. 
The first argument is the URL pattern, the second argument is the view function, and the third argument is the name of the URL pattern. 
The name of the URL pattern is used to refer to the URL pattern in templates and other parts of the Django project."""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls.py')),
]

"""The URL configuration for the accounts app. This file is used to define the URL patterns for the views in the accounts app."""
class DashboardView(LoginRequiredMixin, View):
    @login_required
    def dashboard_view(request):
        ...
        return render(request, 'accounts/templates/accounts/dashboard.html')
    
    @login_required
    def profile_view(request):
        ...
        return render(request, 'accounts/templates/accounts/profile.html')
    
    @login_required
    def change_password_view(request):
        ...
        return render(request, 'accounts/templates/accounts/change_password.html')
    
    @login_required
    def forgot_password_view(request):
        ...
        return render(request, 'accounts/templates/accounts/forgot_password.html')
    
    @login_required
    def login_view(request):
        ...
        return render(request, 'accounts/templates/accounts/login.html')
    
    @login_required
    def signup_view(request):
        ...
        return render(request, 'accounts/templates/accounts/signup.html')
    
    