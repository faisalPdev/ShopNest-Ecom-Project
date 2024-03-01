from django.shortcuts import render
from .models import *
# Create your views here.
def Mobile_product_list(request):
    cat=Category.objects.get(title='Mobile,Tablets')
    products=Product.objects.filter(category=cat)
    context={
        'cat':cat,
        'products':products,
        
    }
    return render(request,'shop.html',context)

def laptop_product_list(request):
    cat=Category.objects.get(title='Laptops,Computers')
    products=Product.objects.filter(category=cat)
    context={
        'cat':cat,
        'products':products,
        
    }
    return render(request,'shop.html',context)