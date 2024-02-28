from django.urls import include, path
from . import views

urlpatterns = [
    path('shop/',views.Mobile_product_list,name='mobile'),
    # path('cat/',views.category_list,name= 'categories'),   
]