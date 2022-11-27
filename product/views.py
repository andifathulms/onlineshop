from django.shortcuts import render
from django.views import View

from .models import Product
from .utils import populated_context_subcategory

class SubCategoryViews(View):

    def get(self, request, *args, **kwargs):
        context = {}
        populated_context_subcategory(context)

        context["products"] = Product.objects.filter(sub_category__name=kwargs['type'])
        
        return render(request, 'product/product_list.html', context)
