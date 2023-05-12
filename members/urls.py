"""Определяет схемы URL для Members."""

from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, EditProfilePageView, ShowProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), 
         name='register'),
    path('edit_profile/', UserEditView.as_view(), 
         name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', views.password_success, 
         name='password_success'),
    path('<int:pk>/profile', ShowProfilePageView.as_view(),
         name='user_profile_page'),
    path('<int:pk>/edit_profile_page', EditProfilePageView.as_view(),
         name='edit_profile_page'),
    path('create_user_profile_page', CreateProfilePageView.as_view(),
         name='create_user_profile_page'),
]
