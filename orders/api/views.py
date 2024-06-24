from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.cart import Cart
from orders.api.serializers import OrderSerializer
from orders.models import Order, OrderItem
from users.currentUser import CurrentUser


class OrderCreateView(APIView):
    def post(self, request):
        cart = Cart(request)
        current_user = CurrentUser(request)
        request.data["user"] = current_user.get().id
        request.data["total_cost"] = cart.get_total_price()
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
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOrdersView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        current_user = CurrentUser(request)
        user = current_user.get()
        if user is None:
            return Response({'answer': 'пользователь не залогинен'}, status=status.HTTP_401_UNAUTHORIZED, headers={"charset": "utf-8"})
        orders_out = []
        for order in orders:
            if order.user.id == user.id:
                orders_out.append(order)
        serializer = OrderSerializer(orders_out, many=True)
        return Response(serializer.data)


class OrderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailsView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
