from django.conf import settings
from django.db import models


class Affair(models.Model):
    """Список дел"""
    title = models.CharField(max_length=127, verbose_name='Заголовок')
    text = models.CharField(max_length=2047, verbose_name='Описание', blank=True)
    date_add = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    date_end = models.DateTimeField(verbose_name='Дата выполнения', blank=True, null=True)

    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return f"{self.author.username} - {self.title}"

    class Meta:
        ordering = ("-date_add",)

    @property
    def is_completed(self):
        return self.date_end is not None

    @property
    def is_in_process(self):
        return not self.is_completed
