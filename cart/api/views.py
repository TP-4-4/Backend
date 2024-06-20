from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.api.serializers import CartSerializer
from cart.cart import Cart
from shop.models import Product


class CartAddView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            products = Product.objects.filter(id=product_id)
            if len(products) == 0:
                return Response({"answer" : 'product не найден ' + str(product_id)}, status=status.HTTP_400_BAD_REQUEST, headers={"charset": "utf-8"})
            quantity = serializer.validated_data['quantity']
            override = serializer.validated_data['override']
            cart.add(product=products[0],
                     quantity=quantity,
                     override_quantity=override)
            return Response({"answer" : 'продукт добавлен ' + str(product_id)}, status=status.HTTP_200_OK, headers={"charset": "utf-8"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartChangeQuantityView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            products = Product.objects.filter(id=product_id)
            if len(products) == 0:
                return Response({"answer" : 'product не найден ' + str(product_id)}, status=status.HTTP_400_BAD_REQUEST, headers={"charset": "utf-8"})
            quantity = serializer.validated_data['quantity']
            cart.add(product=products[0],
                     quantity=quantity)
            return Response({"answer" : 'количество продукта изменено ' + str(product_id)}, status=status.HTTP_200_OK, headers={"charset": "utf-8"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartRemoveView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        products = Product.objects.filter(id=product_id)
        if len(products) == 0:
            return Response({"answer" : 'product не найден ' + str(product_id)}, status=status.HTTP_400_BAD_REQUEST, headers={"charset": "utf-8"})
        cart.remove(product=products[0])
        return Response({"answer" : 'продукт удален ' + str(product_id)}, status=status.HTTP_200_OK, headers={"charset": "utf-8"})


class CartDetailView(APIView):
    def get(self, request):
        cart = Cart(request)
        body_items = []
        for item in cart:
            body_items.append({
                "id": item["product"].id,
                "quantity": item["quantity"],
                "price": item["price"],
            })

        body = {"items": body_items, "items_count": len(cart), "total_price": cart.get_total_price()}
        return Response(body, status=status.HTTP_200_OK, headers={"charset": "utf-8"})
