from django.urls import path

from product.views import(
	SubCategoryViews,
) 

app_name = 'product'

urlpatterns = [
	path('category/<str:type>', SubCategoryViews.as_view(), name="product-subcategory"),
]