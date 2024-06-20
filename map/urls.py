# main/urls.py

from django.urls import path
from . import views

app_name = 'map'

urlpatterns = [
    path('', views.index, name='index'),  # Путь к главной странице
    path('get_route_data/<order_id>/', views.get_route_data, name='get_route_data'),
]
