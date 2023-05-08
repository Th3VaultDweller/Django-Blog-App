from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def home (request):
    """Домашняя страница приложения Blogs."""
    return render(request, 'blogs/home.html', {})



