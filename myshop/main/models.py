from django.db import models
from django.contrib.auth.models import User



class Product(models.Model):
    name = models.CharField('Товар',max_length=100)
    price = models.FloatField('Цена', max_length=15)
    description = models.TextField('Описание',max_length=500)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
