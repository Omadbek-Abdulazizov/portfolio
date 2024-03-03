from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    def __str__(self) -> str:
        return self.get_username()

class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.title

class Portfolio(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images')
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    url = models.URLField()
    git_hub = models.URLField()
    
    def __str__(self) -> str:
        return self.title

class Skills(models.Model):
    title = models.CharField(max_length=50)
    degree = models.IntegerField(default=0)
    
    def __str__(self) -> str:
        return self.title

class Slider(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='slider_images')
    
    def __str__(self) -> str:
        return self.title