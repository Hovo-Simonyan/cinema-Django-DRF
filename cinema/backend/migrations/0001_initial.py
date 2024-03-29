# Generated by Django 4.0.3 on 2022-03-28 11:51

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='photos/people/%Y/%m/%d/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Актер',
                'verbose_name_plural': 'Актеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры ',
            },
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('name', models.CharField(max_length=30, verbose_name='Название дня на армянском')),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дны',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя фильма')),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
                ('description', models.TextField(verbose_name='Описание фильма')),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Картинка фильма')),
                ('year', models.DateField(verbose_name='День выхода')),
                ('country', models.CharField(max_length=50, verbose_name='Страна производитель')),
                ('budget', models.IntegerField(verbose_name='Бюджет')),
                ('actors', models.ManyToManyField(to='backend.actor')),
                ('category', models.ManyToManyField(to='backend.category')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ('year',),
            },
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='photos/people/%Y/%m/%d/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Картинка')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.film', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Снимок',
                'verbose_name_plural': 'Снимкы',
            },
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateTimeField(verbose_name='Start Date')),
                ('date_end', models.DateTimeField(verbose_name='End Date')),
                ('language', models.CharField(max_length=20, verbose_name='Язык')),
                ('allow_age', models.SmallIntegerField(verbose_name='Допустимый возраст')),
                ('ticket_coust', models.SmallIntegerField(verbose_name='Цена')),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.day', verbose_name='День')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.film', verbose_name='Кино')),
                ('hall', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.hall', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Лист фильма',
                'verbose_name_plural': 'Лист фильмов',
            },
        ),
        migrations.AddField(
            model_name='film',
            name='producers',
            field=models.ManyToManyField(to='backend.producer'),
        ),
    ]
