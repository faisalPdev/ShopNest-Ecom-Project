from django import template
from cart.models import wishlist
from Product.models import Product

register = template.Library()

@register.simple_tag
def is_in_wishlist(request,productId):
    product=Product.object.get(pid=productId)

    return wishlist.objects.filter(user=request.user, product=product).exists()