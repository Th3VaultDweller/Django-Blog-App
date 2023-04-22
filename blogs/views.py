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
    categories = Category.objects.all()
    ordering = ['-id'] # минус выводит посты на домашней странице в обратном порядке: от самого нового к самому старому

    def get_context_data(self, *args, **kwargs):
        """Отображение всех категорий постов в dropdown меню на домашней странице."""
        category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context ['category_menu'] = category_menu
        return context

def CategoryListView(request):
    category_menu_list = Category.objects.all() # достаёт все названия категорий из Category.models.py
    return render(request, 'category_list.html', 
                  {'category_menu_list': category_menu_list})

def CategoryView(request, categories):
    """Отображение категорий постов."""
    category_posts = Post.objects.filter(category=categories.replace('-', ' '))
    return render(request, 'categories.html', 
                  {'categories': categories.title().replace('-', ' '), 
                   'category_posts': category_posts})

# def CategoryView(request, categories, *args, **kwargs):
#         """Отображение всех категорий постов в dropdown меню на странице с категориями."""
#         category_posts = Post.objects.filter(category=categories.replace('-', ' '))
#         def __init__ (self):
#             category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
#             context = super(CategoryView, self).get_context_data(*args, **kwargs)
#             context ['category_menu'] = category_menu
#             return context, render(request, 'categories.html', 
#                     {'categories': categories.title().replace('-', ' '), 
#                     'category_posts': category_posts})
    
class ArticleDetailView(DetailView):
    """Отображение детальной информации статьи в блоге."""
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        """Отображение всех категорий постов в dropdown меню при нажатии на пост."""
        category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context ['category_menu'] = category_menu
        return context

class AddPostView(CreateView):
    """Создание нового поста в блоге."""
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__' # выводит на странице создания нового поста все поля для заполнения, указанные в модели Post в models.py
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        """Отображение всех категорий постов в dropdown меню при создании нового поста."""
        category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
        context ['category_menu'] = category_menu
        return context
    
class AddCategoryView(CreateView):
    """Создание нового поста в блоге."""
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__' # выводит на странице создания нового поста все поля для заполнения, указанные в модели Post в models.py
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        """Отображение всех категорий постов в dropdown меню при создании новой категории."""
        category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context ['category_menu'] = category_menu
        return context

class UpdatePostView(UpdateView):
    """Позволяет вносить изменения в существующий пост."""
    model = Post
    form_class = UpdatePostForm
    template_name = 'update_post.html'
    # fields = ('title', 'body')

    def get_context_data(self, *args, **kwargs):
        """Отображение всех категорий постов в dropdown меню при внесении изменений в пост."""
        category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context ['category_menu'] = category_menu
        return context

class DeletePostView(DeleteView):
    """Удаление поста."""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        """Отображение всех категорий постов в dropdown меню на странице удаления поста."""
        category_menu = Category.objects.all() # достаёт все названия категорий из Category.models.py
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context ['category_menu'] = category_menu
        return context





