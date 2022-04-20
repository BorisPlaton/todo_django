def get_affairs_list(request, values=None):
    """Возвращает список дел в зависимости от параметра affair_status в URL"""

    affair_status = request.GET.get('affair_status', "")
    if affair_status == 'completed':
        return request.user.get_completed_affairs(*values)
    elif affair_status == 'process':
        return request.user.get_in_process_affairs(*values)

    return request.user.get_affairs_list(*values)

