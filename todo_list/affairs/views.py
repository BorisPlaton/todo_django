from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from affairs.models import Affair
from affairs.services import get_affairs_list


@login_required
def home(request):
    """Личный кабинет пользователя"""
    context = {
        "affairs_list": get_affairs_list(request, values=['title', 'date_add', 'is_completed'])
    }
    return render(request, 'affairs/home.html', context=context)


@login_required
def add_affair(request):
    """Страница добавления нового дела"""
    return render(request, 'affairs/add_affair.html')
