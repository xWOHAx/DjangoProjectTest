# Generated by Django 5.1.5 on 2025-01-15 09:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('total_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Общая сумма')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('status', models.CharField(choices=[('pending', 'В ожидании'), ('processing', 'Обрабатывается'), ('completed', 'Завершён'), ('cancelled', 'Отменён')], default='pending', max_length=50, verbose_name='Статус заказа')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Фото')),
                ('availability', models.CharField(choices=[('in_stock', 'В наличии'), ('out_of_stock', 'Нет в наличии')], default='in_stock', max_length=50, verbose_name='Наличие')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/', verbose_name='Фото профиля')),
                ('points', models.IntegerField(default=0, verbose_name='Баллы')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Локация')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль пользователя',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]
