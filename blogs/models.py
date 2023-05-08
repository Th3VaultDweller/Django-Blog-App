from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    """Репрезентация поста в блоге."""
    category = models.CharField(max_length=100, default='it') # категория поста со значением "IT" по умолчанию
    # для прикрепления картинок к постам
    header_image = models.ImageField(null=True, 
                                     blank=True, 
                                     upload_to='images/') 
    snippet = models.CharField(max_length=100)
    title = models.CharField(max_length=100) # название поста
    title_tag = models.CharField(max_length=100, default='Blog App')
    author = models.ForeignKey(User, on_delete=models.CASCADE) # при удалении темы, все записи по теме также удаляются - это каскадное удаление
    # body = models.TextField(max_length=1000) # текст поста
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts') # кнопка лайка