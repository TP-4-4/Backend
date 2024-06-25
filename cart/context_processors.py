from .cart import Cart


def cart(request):
    return {'cart': Cart.get_current_cart(request)}
