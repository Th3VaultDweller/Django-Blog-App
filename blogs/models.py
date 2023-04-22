from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    """Категория поста в блоге."""
    name = models.CharField(max_length=100) # имя категории
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

class Post(models.Model):
    category = models.CharField(max_length=100, default='it') # категория поста со значением "IT" по умолчанию
    title = models.CharField(max_length=100) # название поста
    title_tag = models.CharField(max_length=100, default='Blog App')
    author = models.ForeignKey(User, on_delete=models.CASCADE) # при удалении темы, все записи по теме также удаляются - это каскадное удаление
    body = models.TextField(max_length=1000) # текст поста
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')