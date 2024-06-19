# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Путь к главной странице
    path('get_route_data', views.get_route_data, name='get_route_data'),
]
