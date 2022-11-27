from django.shortcuts import render, redirect
from django.views import View

from product.utils import populated_color_and_size, get_colorandsize_by_color, populated_context_subcategory
from product.models import SubCategory, Category

class HomePage(View):
    def get(self, request, *args, **kwargs):
        context = {}
        populated_context_subcategory(context)

        return render(request, 'index.html', context)

def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect

