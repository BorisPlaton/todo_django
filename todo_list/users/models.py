from django.contrib.auth.models import AbstractUser
from django.db.models import QuerySet


class User(AbstractUser):

    def get_affairs_list(self, *args):
        """Все дела"""
        if args:
            return self.affair_set.values(*args)
        return self.affair_set.all()

    @property
    def in_process_affairs_amount(self):
        """Количество невыполненных дел"""
        return self.get_in_process_affairs().count()

    def get_in_process_affairs(self, *args):
        """Невыполненные дела"""
        if args:
            return self.affair_set.filter(date_end__isnull=True).values(*args)
        return self.affair_set.filter(date_end__isnull=True)

    @property
    def completed_affairs_amount(self):
        """Количество выполненных дел"""
        return self.get_completed_affairs().count()

    def get_completed_affairs(self, *args):
        """Выполненные дела"""
        if args:
            return self.affair_set.exclude(date_end__isnull=True).values(*args)
        return self.affair_set.exclude(date_end__isnull=True)
