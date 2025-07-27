from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('custom_password_change/', views.custom_password_change, name='custom_password_change'),
    path('profile/', views.profile, name='profile'),
]
