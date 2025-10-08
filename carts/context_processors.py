from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return {}
    try:
        if request.user.is_authenticated:
            # Logged-in users: filter by user
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            # Guests: filter by cart ID
            cart = Cart.objects.filter(cart_id=_cart_id(request)).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart)
            else:
                cart_items = []
        for cart_item in cart_items:
            cart_count += cart_item.quantity
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_count=cart_count)
