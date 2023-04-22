"""Определяет схемы URL для Blogs."""

from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage

from django.views.generic.base import RedirectView

# from . import views

from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView

urlpatterns = [
    # path ('', views.home, name='home'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path ('', HomeView.as_view(), name='home'),
    path ('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail' ), 
    # pk - это primary key - уникальный ключ для каждого поста
    path ('add_post/', AddPostView.as_view(), name='add_post'),
    path ('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path ('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path ('add_category/', AddCategoryView.as_view(), name='add_category'),
    path ('category/<str:categories>/', CategoryView, name='category'),
    path ('category-list/', CategoryListView, name='category-list'),
]