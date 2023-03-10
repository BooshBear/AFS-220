# Generated by Django 4.1.6 on 2023-02-18 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0005_alter_meal_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
