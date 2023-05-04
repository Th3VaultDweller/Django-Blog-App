from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class UserProfile(models.Model):
    """Репрезентация профиля пользователя"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True, 
                                     blank=True, 
                                     upload_to='images/profile_pictures')
    website_url = models.CharField(max_length=255, null=True, blank=True)
    vk_url = models.CharField(max_length=255, null=True, blank=True)
    twitter_url = models.CharField(max_length=255, null=True, blank=True)
    instagram_url = models.CharField(max_length=255, null=True, blank=True)
    github_url = models.CharField(max_length=255, null=True, blank=True)
    steam_url = models.CharField(max_length=255, null=True, blank=True)
    spotify_url = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return str(self.user)

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
    body = RichTextField(blank=True, null=True) # "богатое" поле для написания поста
    date_added = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_posts') # кнопка лайка

    def total_likes(self):
        """Считает, сколько всего было поставлено лайков под постом."""
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        # return reverse('article-detail', args=(str(self.id)))
        return reverse('home')