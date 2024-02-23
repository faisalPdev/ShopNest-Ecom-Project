from django.shortcuts import render
from Home.models import *
# Create your views here.
def home(request):
    slider=Slider.objects.all()[:3]
    banner=Banner.objects.all()[:1]
    subbanner=Subbanner_1.objects.all()[:2]
    context={
        'slider':slider,
        'banner':banner,
        'subbanner':subbanner,
    }
    return render(request,'home.html',context)