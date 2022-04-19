from django.contrib.auth import logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.generic import FormView

from users.forms import UserRegistrationForm, UserLoginForm


def login_user(request):
    """Авторизирирует пользователя"""
    if request.user.is_authenticated:
        return redirect(reverse('affairs:home'))

    form = UserLoginForm(request, data=request.POST or None)
    context = {'form': form}

    if request.POST and form.is_valid():
        login(request, form.get_user())
        return redirect(reverse('affairs:home'))

    return render(request, 'users/login.html', context=context)


def register_user(request):
    """Регистрирует пользователя"""
    form = UserRegistrationForm(data=request.POST or None)
    context = {'form': form}

    if request.POST and form.is_valid():
        form.save()
        return redirect(reverse('affairs:home'))

    return render(request, 'users/registration.html', context=context)


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect(reverse('users:login'))
    return redirect(reverse('affairs:home'))
