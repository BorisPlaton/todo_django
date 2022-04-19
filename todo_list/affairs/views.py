from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    """Личный кабинет пользователя"""
    return render(request, 'affairs/home.html')
