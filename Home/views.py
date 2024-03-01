from django.shortcuts import render
from Home.models import *
from Product.models  import Product,Category
# Create your views here.
def home(request):
    # category=Category.objects.all()
    topdeal=Product.objects.filter(top_deal_the_day=True)
    topfeatured=Product.objects.filter(top_featured_product=True)
    slider=Slider.objects.all()[:3]
    banner=Banner.objects.all()[:1]
    subbanner=Subbanner_1.objects.all()[:2]
    context={
        'topfeatured':topfeatured,
        # 'category':category,
        'topdeal':topdeal,
        'slider':slider,
        'banner':banner,
        'subbanner':subbanner,
    }
    return render(request,'home.html',context)
