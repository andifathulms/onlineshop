from django.contrib import admin

from .models import Cart, ProductContainer, Wishlist

admin.site.register(Cart)
admin.site.register(ProductContainer)
admin.site.register(Wishlist)
