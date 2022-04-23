from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from affairs.forms import CreateAffairForm
from affairs.services import get_affairs_list, save_affair_from_form


@login_required
def home(request):
    """Список записей"""

    context = {
        "affairs_list": get_affairs_list(request, values=['title', 'date_add', 'is_completed', 'pk'])
    }
    return render(request, 'affairs/home.html', context=context)


@login_required
def affair(request, affair_id):
    """Страница записи"""

    return render(request, 'affairs/affair.html')


@login_required
def add_affair(request):
    """Страница добавления нового дела"""
    form = CreateAffairForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.POST and save_affair_from_form(request, form):
        messages.add_message(request, messages.SUCCESS, "Запись сохранена", extra_tags="success")
        return redirect(reverse('affairs:add_affair'))

    return render(request, 'affairs/add_affair.html', context=context)
