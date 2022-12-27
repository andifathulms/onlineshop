from django.urls import path

from product.views import(
	SubCategoryViews,
	ProductDetailView,
	OnClickCart,
	AddToWishlist,
	DeleteFromWishlist,
) 

app_name = 'product'

urlpatterns = [
	path('category/<str:type>', SubCategoryViews.as_view(), name="product-subcategory"),
	path('detail/<int:pk>', ProductDetailView.as_view(), name="product-detail"),
	path('add-to-cart/<int:pk>', OnClickCart.as_view(), name="add-to-cart"),
	path('add-to-wishlist/<int:pk>', AddToWishlist.as_view(), name="add-to-wishlist"),
	path('delete-from-wishlist/<int:pk>', DeleteFromWishlist.as_view(), name="delete-from-wishlist"),
]