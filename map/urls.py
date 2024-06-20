# main/urls.py

from django.urls import path
from . import views
from .views import MapView

app_name = 'map'

urlpatterns = [
    path('', views.index, name='index'),  # Путь к главной странице
    path('get_route_data/<order_id>/', MapView.as_view(), name='get_route_data'),
]
