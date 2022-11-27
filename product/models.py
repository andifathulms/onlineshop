from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    name            = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class SubCategory(models.Model):
    category        = models.ForeignKey('Category', on_delete=models.CASCADE)
    name            = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.category.name + " - " + self.name

class Product(models.Model):
    sub_category    = models.ForeignKey('SubCategory', on_delete=models.CASCADE)
    title           = models.CharField(max_length=255)
    description     = models.TextField(blank=True, null=True)
    material_desc   = models.CharField(max_length=255, blank=True, null=True)
    lengan_desc     = models.CharField(max_length=255, blank=True, null=True)
    size_desc       = models.TextField(blank=True, null=True)
    price           = models.PositiveIntegerField()
    discount        = models.PositiveIntegerField(default=0)
    image           = models.ManyToManyField('ImageProduct', blank=True)

    def __str__(self) -> str:
        return self.sub_category.name + " - " + self.title
    
    def realPrice(self):
        return round(self.price*(100-self.discount)/100)

class Size(models.Model):
    name            = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name

class Color(models.Model):
    name            = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class ColorAndSize(models.Model):
    color           = models.ForeignKey(Color, on_delete=models.CASCADE)
    size            = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.color.name + " - " + self.size.name

class ColorAndSizeAvailability(models.Model):
    product         = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_cs')
    color_and_size  = models.ForeignKey('ColorAndSize', on_delete=models.CASCADE)
    count           = models.IntegerField(default=0)
    available       = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.product.__str__() + " - " + self.color_and_size.__str__() + " - " + str(self.count)

class ImageProduct(models.Model):
    image = models.ImageField(upload_to='prduct', blank=True, null=True)
    color = models.ForeignKey('Color', on_delete=models.CASCADE, blank=True, null=True)

@receiver(post_save, sender=Product)
def set_intial_csavailability(sender, instance, created, **kwargs):
    if created:
        pass