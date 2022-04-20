from django.conf import settings
from django.db import models


class Affair(models.Model):
    """Список дел"""
    title = models.CharField(max_length=128, verbose_name='Заголовок')
    text = models.TextField(max_length=2048, verbose_name='Описание', blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    date_end = models.DateTimeField(verbose_name='Дата выполнения', blank=True, null=True)
    is_completed = models.BooleanField(verbose_name='Задание выполнено', default=False)

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f"{self.author.username} - {self.title}"

    class Meta:
        ordering = ("-date_add",)
