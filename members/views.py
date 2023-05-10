from typing import Any, Optional
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from blogs.models import UserProfile

# Create your views here.


class ShowProfilePageView(DetailView):
    """Показывает профиль пользователя блога."""
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = UserProfile.objects.all() # достаёт все профили из db

        # достаёт конкретный профиль пользователя из db по pk
        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])
        context = super(ShowProfilePageView,
                        self).get_context_data(*args, **kwargs)
        context['page_user'] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    """Позволяет редактировать профиль пользователя блога."""
    model = UserProfile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 
              'profile_picture', 
              'nickname', 
              'first_name',
              'last_name',
              'email_address',
              'website_url',
              'vk_url',
              'twitter_url',
              'instagram_url',
              'github_url',
              'steam_url',
              'spotify_url'
              ]   
    success_url = reverse_lazy('home')


class UserRegisterView(generic.CreateView):
    """Форма для регистрации новых пользователей блога."""
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    """Форма для редактирования информации существующих пользователей блога."""
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    """Форма для смены пароля учётной записи в блоге."""
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')


def password_success(request):
    """Сообщает пользователю об удачной смене пароля."""
    return render(request, 'registration/password_success.html', {})
