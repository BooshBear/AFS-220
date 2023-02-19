from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=225)
    slug = models.SlugField(null=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name



class Meal(models.Model):
    category = models.ForeignKey(Category, related_name='meals', on_delete=models.CASCADE, default=False, null=True)
    name = models.CharField(max_length=225)
    slug = models.SlugField(null=True)
    price = models.FloatField(null=True)
    image = models.ImageField(upload_to='meal_images', blank=True, null=True)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name