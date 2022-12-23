from django.db import models

from model_utils import Choices

from account.models import Customer, Address
from product.models import Product, ColorAndSize

class Cart(models.Model):
    customer           = models.OneToOneField(Customer, related_name='orders', on_delete=models.CASCADE)
    products           = models.ManyToManyField('ProductContainer', related_name='orders', blank=True, null=True)

    def __str__(self) -> str: 
        return self.customer.account.username + " #" + str(self.id)
    
    @property
    def calculate_raw_price(self):
        return sum([x.quantity * x.product.price for x in self.products.select_related('product').all()])
    
    @property
    def calculate_discount_amount(self):
        return sum([x.quantity * x.product.discount_amount for x in self.products.select_related('product').all()])
    
    def calculate_total_price(self):
        return self.calculate_raw_price - self.calculate_discount_amount

    def addToCart(self, product, quantity, color_and_size):
        container = ProductContainer(product=product, quantity=quantity, color_and_size=color_and_size)
        container.save()

        self.products.add(container)
        self.save()
    
    def isInCart(self, product):
        return product in [container.product for container in self.products.all()]


class ProductContainer(models.Model):
    product         = models.ForeignKey(Product, related_name='product_container', on_delete=models.CASCADE)
    color_and_size  = models.ForeignKey(ColorAndSize, on_delete=models.CASCADE, blank=True, null=True)
    quantity        = models.PositiveIntegerField(default=1)


class Shipper(models.Model):
    name            = models.CharField(max_length=20)

class Wishlist(models.Model):
    customer        = models.OneToOneField(Customer, related_name='wishlist', on_delete=models.CASCADE)
    products        = models.ManyToManyField(Product, related_name='wishlist', blank=True, null=True)
    date_added      = models.DateTimeField(auto_now_add=True)