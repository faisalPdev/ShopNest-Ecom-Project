from django.db import models
from userauth.models import Account
from Product.models import Product

from shortuuid.django_fields import ShortUUIDField

# Create your models here.

class Coupon(models.Model):
    code=models.CharField(max_length=50)
    discount_percentage=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.code
    
class Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    discount=models.DecimalField(max_digits=10,decimal_places=2,default=0,blank=True)
    coupon=models.ForeignKey(Coupon,on_delete=models.SET_NULL,null=True,blank=True)
    cart_id=ShortUUIDField(unique=True,length=10,max_length=30,alphabet="abcdefgh12345")

    
    def __str__(self):
        return str(self.id)
    



class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1) 
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.product} in {self.cart}"
    
    def total(self):
        return self.quantity * self.product.price
    


   


    

class CouponUsed(models.Model):
    coupon=models.ForeignKey(Coupon,on_delete=models.CASCADE)   
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    used_at=models.DateTimeField(auto_now_add=True)
   
    discounted_amount=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return f"{self.coupon} used by {self.user}"



class wishlist(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"wishlist of{self.user}"