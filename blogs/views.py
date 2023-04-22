from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdatePostForm
from django.urls import reverse_lazy

# Create your views here.

# def home (request):
#     """Домашняя страница приложения Blogs."""
#     return render(request, 'blogs/home.html', {})

class HomeView(ListView):
    """Домашняя страница приложения Blogs со всеми постами."""
    model = Post
    template_name = 'home.html'
    ordering = ['-id'] # минус выводит посты на домашней странице в обратном порядке: от самого нового к самому старому

def CategoryView(request, categories):
    category_posts = Post.objects.filter(category=categories)
    return render(request, 'categories.html', 
                  {'categories': categories, 
                   'category_posts': category_posts})

class ArticleDetailView(DetailView):
    """Отображение детальной информации статьи в блоге."""
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    """Создание нового поста в блоге."""
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' # выводит на странице создания нового поста все поля для заполнения, указанные в модели Post в models.py
    # fields = ('title', 'body')

class AddCategoryView(CreateView):
    """Создание нового поста в блоге."""
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__' # выводит на странице создания нового поста все поля для заполнения, указанные в модели Post в models.py
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):
    """Позволяет вносить изменения в существующий пост."""
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    # fields = ('title', 'body')

class DeletePostView(DeleteView):
    """Удаление поста."""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')





