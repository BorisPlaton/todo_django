from django.conf import settings
from django.db import models


class Affair(models.Model):
    title = models.CharField(max_length=127, verbose_name='Заголовок')
    text = models.CharField(max_length=2047, verbose_name='Список дел')
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    date_end = models.DateTimeField(null=True, verbose_name='Дата выполнения')

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')