from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    """Создание формы для добавления нового поста в блог."""
    class Meta:
        model = Post
        fields = ('category', 'title', 'author', 'body')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the title of your post here!'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'User', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something sick!'}),
        }

class UpdatePostForm(forms.ModelForm):
    """Создание формы для внесения изменений в существующий пост."""
    class Meta:
        model = Post
        fields = ('category', 'title', 'body')

        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type the title of your post here!'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something sick!'}),
        }