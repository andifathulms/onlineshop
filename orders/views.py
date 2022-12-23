from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from product.utils import populated_context_subcategory
from product.models import Product

class CartView(View, LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        context = {}
        populated_context_subcategory(context)

        last_seen_id = request.user.user_customer.returnCleanLastView()
        cart_products = request.user.user_customer.orders.products

        clauses = ' '.join(['WHEN id=%s THEN %s' % (pk, i) for i, pk in enumerate(last_seen_id)])
        ordering = 'CASE %s END' % clauses

        context["products_in_cart"] = cart_products.count()
        context["cart_products"] = cart_products.all()
        context["products"] = Product.objects.filter(pk__in=last_seen_id).extra(select={'ordering': ordering}, order_by=('ordering',))
        context["cart"] = request.user.user_customer.orders
        
        return render(request, 'orders/cart.html', context)