from .models import Cart, ProductContainer

def getUserCart(user):
    return Cart.objects.prefetch_related('products').get(customer=user)