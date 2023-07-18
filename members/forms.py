from typing import Any
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogs.models import UserProfile

class ProfilePageForm(forms.ModelForm):
    """Форма для создания профиля пользователя блога."""
    class Meta:
        model = UserProfile
        fields = ('bio', 
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
        )
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tell the world about yourself'}),

            # 'profile_picture': forms.ImageField(attrs={'class':'form-control'}),

            'nickname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Make it look cool!'}),

            'first_name': forms.TextInput(attrs={'class': 'form-control'}),

            'last_name': forms.TextInput(attrs={'class': 'form-control'}),

            'email_address': forms.TextInput(attrs={'class': 'form-control'}),

            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            
            'vk_url': forms.TextInput(attrs={'class': 'form-control'}),

            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),

            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),

            'github_url': forms.TextInput(attrs={'class': 'form-control'}),

            'steam_url': forms.TextInput(attrs={'class': 'form-control'}),

            'spotify_url': forms.TextInput(attrs={'class':'form-control'}),
        }

class SignUpForm(UserCreationForm):
    """Продвинутая форма для регистрации пользователей блога."""
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
                  'password1',
                  'password2')

    def __init__(self, *args, **kwargs):
        """Функция, позволяющая красиво отобразить поля Username, Password1 и Password2."""
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    """Форма для редактирования профилей пользователей блога."""
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    # last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # is_superuser = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_staff = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # is_active = forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    # date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password')


class PasswordChangingForm(PasswordChangeForm):
    """Форма смены пароля."""
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
