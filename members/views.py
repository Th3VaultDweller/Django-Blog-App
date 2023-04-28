from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm

# Create your views here.

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

