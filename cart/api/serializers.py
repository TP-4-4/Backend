from rest_framework import serializers

from shop.models import Product


class CartSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField()
    override = serializers.BooleanField(required=False)

    class Meta:
        model = Product
        fields = ["quantity", "override"]
