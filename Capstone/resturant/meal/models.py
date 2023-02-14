from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name



class Meal(models.Model):
    category = models.ForeignKey(Category, related_name='meals', on_delete=models.CASCADE, default=False, null=True)
    name = models.CharField(max_length=225)
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to='meal_images', blank=True, null=True)
    
    def __str__(self):
        return self.name