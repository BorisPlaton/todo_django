from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from affairs.forms import CreateAffairForm, AffairEditingForm
from affairs.models import Affair
from affairs.services import get_affairs_list, save_affair_from_form, update_affair_from_form, delete_affair


@login_required
def home(request):
    """Список записей"""

    context = {
        "affairs_list": get_affairs_list(request,
                                         values_list=['title', 'date_add', 'is_completed', 'pk', 'date_end'])
    }
    return render(request, 'affairs/home.html', context=context)


@login_required
def affair_view(request, affair_id):
    """Страница записи"""

    affair = Affair.objects.filter(pk=affair_id, author__pk=request.user.pk).first()
    if not affair:
        return redirect('affairs:home')

    form = AffairEditingForm(request.POST or None, instance=affair)
    context = {
        'form': form,
        'affair': affair
    }

    if request.POST and request.POST.get('save'):
        update_affair_from_form(request, form)
        return redirect('affairs:affair', affair_id)
    elif request.POST.get('delete'):
        messages.add_message(request, messages.SUCCESS, "Запись удалена", extra_tags="warning")
        delete_affair(affair_id)
        return redirect('affairs:home')

    return render(request, 'affairs/affair.html', context=context)


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
