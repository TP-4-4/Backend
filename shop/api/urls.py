from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('products/',
         views.ProductListView.as_view(),
         name='product_list'),
    path('products/<pk>/',
         views.ProductDetailView.as_view(),
         name='product_detail'),
    path('categories/',
         views.CategoryView.as_view(),
         name='category_list'),
    path('categories/<pk>/',
         views.CategoryDetailView.as_view(),
         name='category_detail'),
]