from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from orders.api.serializers import OrderSerializer
from orders.models import Order, OrderItem


class OrderCreateView(APIView):
    def post(self, request):
        cart = Cart(request)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()

            response = Response({"answer": 'order сделан ' + str(order.id)})
            response.headers = {"charset": "utf-8"}
            response.status_code = 200
            return response


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailsView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
