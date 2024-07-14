
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone
from django.db import models
from userauth.models import Account,Address
from Product.models import Product

# Create your models here.

class  Order(models.Model):
    
    ORDER_STATUS=[
        ('Pending','Pending'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
    ]

    PAYMENT_STATUS=[
        ('Pending','Pending'),
        ('Processing','Processing'),
        ('Paid','Paid'),
        ('Failed','Failed'),
    ]

    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    payment_mode=models.CharField(max_length=100)
    order_id=ShortUUIDField(unique=True,length=10,max_length=30,prefix="prod",alphabet="abcdefgh12345")  
    order_date=models.DateTimeField(null=True,blank=True)
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default="Pending")
    payment_status=models.CharField(max_length=20,choices=PAYMENT_STATUS,default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id
    

class OrderItem(models.Model):
    ORDER_STATUS=[
        ('Pending','Pending'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
    ]
    order_item_id=ShortUUIDField(unique=True,length=10,max_length=30,prefix="item",alphabet="abcdefgh12345")
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    order_status=models.CharField(max_length=20,choices=ORDER_STATUS,default="Pending")
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.product} in Order {self.order}"
    

class PaymentDetails(models.Model):
    payment_id=ShortUUIDField(unique=True,length=10,max_length=30,prefix="pay",alphabet="abcdefgh12345")
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    payment_mode=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment Detail of {self.order}"


