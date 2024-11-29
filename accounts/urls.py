from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name='home'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    
    path('dashboard/', views.dashboard_views, name='dashboard'),
]
