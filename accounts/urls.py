from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name='home'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('generate_otp/', views.generate_otp, name='generate_otp'),
    
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password_view, name='reset_password'),
    
    path('dashboard/', views.dashboard_views, name='dashboard'),
    path('profile/', views.profile_views, name='profile'),
    path('profile/change-password/', views.change_password_view, name='change_password'),
]
