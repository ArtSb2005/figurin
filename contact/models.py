from django.db import models

# Create your models here.
from django.urls import reverse


class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    group = models.CharField(max_length=6, verbose_name='Группа')
    email = models.EmailField(max_length=200, verbose_name='Почта')
    message = models.TextField(max_length=1000, verbose_name='Обращение')

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Обратную связь'
        verbose_name_plural = 'Обратная связь'

    def get_absolute_url(self):
        return reverse('contact')