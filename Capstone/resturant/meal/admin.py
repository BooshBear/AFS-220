from django.contrib import admin

# Register your models here.

from .models import Category, Meal

admin.site.register(Category)
admin.site.register(Meal)