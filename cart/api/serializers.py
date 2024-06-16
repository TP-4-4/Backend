from rest_framework import serializers
from shop.models import Product


class CartAddSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    override = serializers.BooleanField()
    class Meta:
        model = Product
        fields = ["quantity", "override"]


