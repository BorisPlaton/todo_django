from django.contrib import admin
from django.urls import path, include

from todo_list.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('affairs/', include('affairs.urls'))
]
