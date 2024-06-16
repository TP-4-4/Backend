from rest_framework.response import Response
from rest_framework.views import APIView

from cart.api.serializers import CartAddSerializer
from cart.cart import Cart
from shop.models import Product


class CartAddView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        serializer = CartAddSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.filter(id=product_id)[0]
            quantity = serializer.validated_data['quantity']
            override = serializer.validated_data['override']
            cart.add(product=product,
                     quantity=quantity,
                     override_quantity=override)
            response = Response({"answer" : 'product добавлен ' + str(product_id)})
            response.headers = {"charset" : "utf-8"}
            response.status_code = 200
            return response


class CartRemoveView(APIView):
    def post(self, request, product_id):
        cart = Cart(request)
        product = Product.objects.filter(id=product_id)[0]
        cart.remove(product=product)
        response = Response({"answer" : 'product удален ' + str(product_id)})
        response.headers = {"charset" : "utf-8"}
        response.status_code = 200
        return response


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

        body = {"items": body_items, "total_price": cart.get_total_price()}
        response = Response(body)
        response.headers = {"charset" : "utf-8"}
        response.status_code = 200
        return response
