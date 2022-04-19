from django.urls import path

from affairs import views

app_name = 'affairs'

urlpatterns = [
    path('', views.home, name="home")
]