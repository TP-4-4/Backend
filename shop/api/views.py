from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.api.serializers import ProductSerializer, CategorySerializer
from shop.models import Product, Category


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        products = Product.objects.all()
        products_out = []
        for product in products:
            if product.category.id == int(pk):
                products_out.append(product)
        serializer = ProductSerializer(products_out, many=True)
        return Response(serializer.data)
