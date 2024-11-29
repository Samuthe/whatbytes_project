from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_views, name='home'),

    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    
    path('dashboard/', views.dashboard_views, name='dashboard'),
]
