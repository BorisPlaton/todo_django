from django.urls import path

from affairs import views
from affairs.views import add_affair

app_name = 'affairs'

urlpatterns = [
    path('', views.home, name="home"),
    path(r'^add_affair/$', add_affair, name='add_affair'),
]
