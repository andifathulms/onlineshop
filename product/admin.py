from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description', 'size_desc', )

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(ColorAndSize)
admin.site.register(ColorAndSizeAvailability)
admin.site.register(Product, ProductAdmin)
admin.site.register(ImageProduct)