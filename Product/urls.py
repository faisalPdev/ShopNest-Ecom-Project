from django.urls import include, path
from . import views

urlpatterns = [
    path('shop/mobile_tablets/',views.Mobile_product_list,name='mobile_tablets'),
    path('shop/laptops_computers/',views.laptop_product_list,name='laptops_computers'),
    # path('cat/',views.category_list,name= 'categories'),   
]