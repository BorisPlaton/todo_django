from django.urls import path

from affairs import views
from affairs.views import add_affair, affair_view

app_name = 'affairs'

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:affair_id>/', views.affair_view, name='affair'),
    path(r'add_affair/', add_affair, name='add_affair'),
]
