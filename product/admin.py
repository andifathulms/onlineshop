from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ColorAndSize)
admin.site.register(ColorAndSizeAvailability)
admin.site.register(Product)
admin.site.register(ImageProduct)