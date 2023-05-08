"""Определяет схемы URL для Blogs."""

from django.urls import path

from django.contrib.staticfiles.storage import staticfiles_storage

from django.views.generic.base import RedirectView

from . import views

# from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    # path ('', views.home, name='home'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico'))),
    path ('', views.home, name='category-list'),
]