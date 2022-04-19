from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    @property
    def in_process_affairs_amount(self):
        """Количество невыполненных дел"""
        return self.in_process_affairs.count()

    @property
    def in_process_affairs(self):
        """Невыполненные дела"""
        return self.affair_set.filter(date_end__isnull=True)

    @property
    def completed_affairs_amount(self):
        """Количество выполненных дел"""
        return self.completed_affairs.count()

    @property
    def completed_affairs(self):
        """Выполненные дела"""
        return self.affair_set.exclude(date_end__isnull=True)
