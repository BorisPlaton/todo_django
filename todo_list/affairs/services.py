import datetime

from affairs.models import Affair


def get_affairs_list(request, values_list: list = None):
    """
    Возвращает QuerySet списка дел с полями из списка values,
    по умолчанию включает все поля, в зависимости от параметра
    affair_status в URL.
    """

    affair_status = request.GET.get('affair_status', "")
    if affair_status == 'completed':
        return request.user.get_completed_affairs(*values_list)
    elif affair_status == 'process':
        return request.user.get_in_process_affairs(*values_list)

    return request.user.get_affairs_list(*values_list)


def save_affair_from_form(request, form):
    """Сохраняет запись из ModelForm"""

    if form.is_valid():
        affair = form.save(commit=False)
        affair.author = request.user
        affair.save()
        return affair


def update_affair_from_form(request, form):
    """Обновляет запись Affair из ModelForm"""

    if form.has_changed() and form.is_valid():
        affair = form.save(commit=False)
        if affair.is_completed:
            affair.date_end = datetime.datetime.utcnow()
        else:
            affair.date_end = None
        affair.save()


def delete_affair(affair_id):
    """Удалять запись из модели Affair"""

    Affair.objects.get(pk=affair_id).delete()
