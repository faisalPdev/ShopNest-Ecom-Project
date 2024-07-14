from django.contrib import admin
from cart.models import Cart,CartItem,Coupon,wishlist,CouponUsed
# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(Coupon)
admin.site.register(CouponUsed)
admin.site.register(wishlist)
