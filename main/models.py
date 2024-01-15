from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Направление')
    description = models.TextField(**NULLABLE, verbose_name="Описание категории")
    phot = models.ImageField(upload_to='serv/', **NULLABLE, verbose_name='Фото')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Services(models.Model):
    name_serv = models.CharField(max_length=100, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # phot = models.ImageField(upload_to='serv/', **NULLABLE, verbose_name='Фото')
    price = models.CharField(max_length=50, verbose_name='Цена')
    serv_description = models.TextField(max_length=400, verbose_name='Описание услуги')

    def __str__(self):
        return f'{self.name_serv} ({self.category})'

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'





# Create your models here.
