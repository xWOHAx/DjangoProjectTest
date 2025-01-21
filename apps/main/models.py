from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    category = models.ForeignKey(
    'Category',
    on_delete=models.CASCADE,
    related_name='products',
    verbose_name='Категория'
)
    photo = models.ImageField(upload_to='images/' ,verbose_name='Фото')
    availability = models.CharField(
    max_length=50,
    choices=[
        ('in_stock', 'В наличии'),
        ('out_of_stock', 'Нет в наличии'),
    ],
    default='in_stock',
    verbose_name='Наличие'
)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"
