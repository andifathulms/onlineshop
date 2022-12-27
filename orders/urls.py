from django.urls import path

from orders.views import(
	CartView,
	WishlistView,
) 

app_name = 'orders'

urlpatterns = [
	path('cart', CartView.as_view(), name="cart"),
	path('wishlist', WishlistView.as_view(), name="wishlist"),
]
