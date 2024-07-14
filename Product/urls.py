from django.urls import include, path
from . import views

urlpatterns = [
    path('shop/mobile_tablets/',views.Mobile_product_list,name='mobile_tablets'),
    path('shop/laptops_computers/',views.laptop_product_list,name='laptops_computers'),
    path('shop/product-modal/<pid>',views.product_modal,name='product_modal'),
    path('shop/product-detail/<slug>',views.product_detail,name='product_detail'),
    # path('cat/',views.category_list,name= 'categories'),   
]