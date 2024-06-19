from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/',
         views.OrderView.as_view(),
         name='order_list'),
    path('orders/<pk>/',
         views.OrderDetailsView.as_view(),
         name='order_details'),
    path('userOrders/',
         views.UserOrdersView.as_view(),
         name='user_orders'),
]