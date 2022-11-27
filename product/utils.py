import itertools
from .models import Size, Color, ColorAndSize, SubCategory

def populated_color_and_size():
    size = list(Size.objects.all())
    color = list(Color.objects.all())

    pairing = list(itertools.product(size,color))
    for pair in pairing:
        try:
            cs = ColorAndSize.objects.get(size=pair[0],color=pair[1])
        except:
            cs = ColorAndSize(size=pair[0], color=pair[1])
            cs.save()

def get_colorandsize_by_color(color):
    try: 
        return ColorAndSize.objects.filter(color = Color.objects.get(name=color))
    except:
        None

def get_colorandsize_by_size(size):
    try:
        return ColorAndSize.objects.filter(size = Size.objects.get(name=size))
    except:
        None

def populated_context_subcategory(context):
    context["basiba_sub"] = SubCategory.objects.filter(category__name="Basiba Series")
    context["hijab_sub"] = SubCategory.objects.filter(category__name="Hijab")
    context["collection_sub"] = SubCategory.objects.filter(category__name="Collection")