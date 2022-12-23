from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product, SubCategory, ColorAndSizeAvailability, Color, Size, ColorAndSize
from .utils import populated_context_subcategory
from orders.utils import getUserCart

import collections

class SubCategoryViews(View):

    def get(self, request, *args, **kwargs):
        context = {}
        populated_context_subcategory(context)

        context["subcategory"] = SubCategory.objects.get(name=kwargs['type'])
        context["products"] = Product.objects.prefetch_related('product_cs').filter(sub_category__name=kwargs['type'])
        for product in context["products"]:
            for cs in product.product_cs.all():
                print(product, cs)
        
        return render(request, 'product/product_list.html', context)

class ProductDetailView(View):

    def get(self, request, *args, **kwargs):
        context = {}
        populated_context_subcategory(context)
        
        product = Product.objects.prefetch_related('product_cs').get(pk=kwargs['pk'])
        context["product"] = product

        color_and_size = ColorAndSizeAvailability.objects.select_related('product').filter(product=product)
        
        dict_x = collections.defaultdict(list)
        for cs in color_and_size:
            dict_x[cs.color_and_size.color].append(cs.color_and_size.size)
        
        context["color_and_size"] = dict_x.items()

        # Add this item to last view
        request.user.user_customer.addToLastView(product.id)

        # Check if this item in user cart
        cart = getUserCart( request.user.user_customer)
        context["in_cart"] = cart.isInCart(product)

        return render(request, 'product/product_detail.html', context)

    def post(self, request, *args, **kwargs):
        context = {}
        populated_context_subcategory(context)
        
        product = Product.objects.get(pk=kwargs['pk'])
        context["product"] = product

        data = request.POST
        this_product = Product.objects.get(id=int(data['productId']))
        quantity = data['quantity']
        cart = getUserCart( request.user.user_customer)
        cart.addToCart(this_product,quantity)
        context["in_cart"] = cart.isInCart(product)

        return render(request, 'product/product_detail.html', context)

class OnClickCart(View, LoginRequiredMixin):

    def post(self, request, *args, **kwargs):
        context = {}
        
        product = Product.objects.get(pk=kwargs['pk'])
        context["product"] = product

        data = request.POST
        this_product = Product.objects.get(id=int(data['productId']))
        quantity = data['quantity']

        if data['colorId'] == '' or data['sizeId'] == '':
            context['error'] = True
            return render(request, 'product/snippets/partial/add_to_cart.html', context)
        
        color = Color.objects.get(id=int(data['colorId']))
        size = Size.objects.get(id=int(data['sizeId']))
        color_and_size = ColorAndSize.objects.get(color=color, size=size)
        context['color'] = color
        context['size'] = size
        
        cart = getUserCart(request.user.user_customer)
        cart.addToCart(this_product,quantity,color_and_size)

        return render(request, 'product/snippets/partial/add_to_cart.html', context)

class AddToWishlist(View, LoginRequiredMixin):
    
    def post(self, request, *args, **kwargs):
        context = {}

        product = Product.objects.get(pk=kwargs['pk'])
        context["product"] = product
        wishlist = request.user.user_customer.wishlist
        wishlist.products.add(product)
        return render(request, 'product/snippets/partial/add_to_wishlist.html', context)

