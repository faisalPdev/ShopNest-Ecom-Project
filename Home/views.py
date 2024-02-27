from django.shortcuts import render
from Home.models import *
from Product.models  import Product,Category
# Create your views here.
def home(request):

    topdeal=Product.objects.filter(top_deal_the_day=True)
    slider=Slider.objects.all()[:3]
    banner=Banner.objects.all()[:1]
    subbanner=Subbanner_1.objects.all()[:2]
    context={
        'topdeal':topdeal,
        'slider':slider,
        'banner':banner,
        'subbanner':subbanner,
    }
    return render(request,'home.html',context)

# def homeCategory(request):
#     category=Category.objects.get(cid=cat2bgc5f2f3d)
#     context={
#         'category':category,
#     }
#     return render(request,'home.html')