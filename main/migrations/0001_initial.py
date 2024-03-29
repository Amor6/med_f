# Generated by Django 5.0.1 on 2024-01-13 13:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Направление')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание категории')),
                ('phot', models.ImageField(blank=True, null=True, upload_to='serv/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_offer', models.CharField(max_length=100, verbose_name='Предложение')),
                ('pay', models.CharField(max_length=250, verbose_name='Стоимость')),
                ('offer_description', models.TextField(max_length=300, verbose_name='Описание предложения')),
            ],
            options={
                'verbose_name': 'Название предложения',
                'verbose_name_plural': 'Название предложений',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_serv', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.CharField(max_length=50, verbose_name='Цена')),
                ('serv_description', models.TextField(max_length=400, verbose_name='Описание услуги')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
