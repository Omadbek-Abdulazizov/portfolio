from django.contrib import admin
from .models import Category, Portfolio,Skills, Slider

# Register your models here.
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Skills)
admin.site.register(Slider)