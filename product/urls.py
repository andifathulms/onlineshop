from django.urls import path

from product.views import(
	SubCategoryViews,
	ProductDetailView,
) 

app_name = 'product'

urlpatterns = [
	path('category/<str:type>', SubCategoryViews.as_view(), name="product-subcategory"),
	path('detail/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
]