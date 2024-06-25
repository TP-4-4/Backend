from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart:
    @staticmethod
    def create_if_empty(request):
        print("INVOKE CART")
        cart = request.session.get(settings.CART_SESSION_ID)
        if not cart:
            print("NEW SESSION, EMPTY CART")
            request.session[settings.CART_SESSION_ID] = {}

    @staticmethod
    def add(request, product, quantity=1, override_quantity=False):
        Cart.create_if_empty(request)
        cart = request.session.get(settings.CART_SESSION_ID)
        product_id = str(product.id)
        if product_id not in cart:
            cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            cart[product_id]['quantity'] = quantity
        else:
            cart[product_id]['quantity'] += quantity
        request.session.modified = True

    @staticmethod
    def remove(request, product):
        Cart.create_if_empty(request)
        cart = request.session.get(settings.CART_SESSION_ID)
        product_id = str(product.id)
        if product_id in cart:
            del cart[product_id]
            request.session.modified = True

    @staticmethod
    def get_current_cart(request):
        Cart.create_if_empty(request)
        cart = request.session.get(settings.CART_SESSION_ID)
        product_ids = cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_to_display = cart.copy()
        for product in products:
            cart_to_display[str(product.id)]['product'] = product
        for item in cart_to_display.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
        return cart_to_display

    @staticmethod
    def get_total_quantity(request):
        Cart.create_if_empty(request)
        cart = request.session.get(settings.CART_SESSION_ID)
        return sum(item['quantity'] for item in cart.values())

    @staticmethod
    def get_total_price(request):
        Cart.create_if_empty(request)
        cart = request.session.get(settings.CART_SESSION_ID)
        return sum(Decimal(item['price']) * item['quantity'] for item in cart.values())

    @staticmethod
    def clear(request):
        Cart.create_if_empty(request)
        del request.session[settings.CART_SESSION_ID]
        request.session.modified = True
