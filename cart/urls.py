from django.urls import include, path
from . import views

urlpatterns = [
   
    path('add_to_cart', views.addToCartView, name='add_to_cart'),
    path('', views.cartView, name='cart'),
    path('cart-item-decrement', views.CartQtyDecrement, name='cart-item-decrement'),
    path('cart-item-increment', views.CartQtyIncrement, name='cart-item-increment'),
    path('remove-item', views.removeItem, name='remove-item'),
    path('wishlist', views.wishlistView, name='wishlist'),
    path('add_to_wishlist', views.wishlistAdd, name='add_to_wishlist'),
    path('place-order/', views.place_order, name='place-order'),
    path('coupon_apply/',views.coupon_apply, name='coupon_apply'),


    
]