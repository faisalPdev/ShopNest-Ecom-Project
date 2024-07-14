from django.shortcuts import render
from decimal import Decimal
from Product.models import Product
from . import models as cartmodels
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
# Create your views here.

def addToCartView(request):

    if request.method == "POST":
        if request.user.is_authenticated:

            user=request.user
            pid=request.POST.get('pid')
            product_qty=request.POST.get('product_qty')
            
            product=Product.objects.get(pid=pid)
            # check if the user already have a cart if not create one

            cart, created = cartmodels.Cart.objects.get_or_create(user=user)


            # check if the user already have this product in the cart if not add it

            cart_item=cartmodels.CartItem.objects.filter(cart=cart,product=product).first()

            if cart_item:
                messages.warning(request,"product is already in the cart")
                return JsonResponse({"message":"product is already in the cart"})
            else:
                cartmodels.CartItem.objects.create(
                   cart=cart,
                   product=product,
                   quantity=product_qty,    
                )
                messages.success(request,"added to cart")
                return JsonResponse({"message":"added to cart"})
        else:
            pid=request.POST.get('pid')
            product_qty=request.POST.get('product_qty')
            Cart=request.session.get('cart',{})
            if str(pid) in Cart:
                return JsonResponse({"message":"product is already in the cart"})
            else:
                Cart[str(pid)]=product_qty
                request.session['cart']=Cart
                return JsonResponse({"message":"added to cart"})
                
    return JsonResponse({'error': 'Invalid request'}, status=400)


# def cartView(request):
#     sub_total=0
#     if request.user.is_authenticated:
#         user=request.user
#         cart=models.cart.objects.filter(user=user)
#         sub_total=0
#         for item in cart:
#             sub_total=item.total() + sub_total
        
            

#         context={
#             'cart':cart,
#             'sub_total':sub_total,
#         }
#     else:
#         session_cart = request.session.get('cart', {})
#         cart_list = []

#         for pid, qty in session_cart.items():
#             try:
#                 product = Product.objects.get(pid=pid)
                
#                 cart_list.append({
#                     'product': product,
#                     'quantity': qty,
#                     'total': product.price * qty,
                    
#                 })
              
#             except Product.DoesNotExist:
#                 continue  # If the product doesn't exist, skip it
        
#         context = {
#             'cart': cart_list,
#             'sub_total': sub_total,
#         }

#     return render(request, 'cart.html', context)

def cartView(request):
    sub_total = 0

    if request.user.is_authenticated:
        user = request.user

        cart,created=cartmodels.Cart.objects.get_or_create(user=user)

        cart_items=cartmodels.CartItem.objects.filter(cart=cart)
        
        for item in cart_items:
            sub_total += item.total()
            
        cart.total_amount=Decimal(cart.total_amount) + sub_total
        cart.save()

        context = {
            'cart': cart_items,
            'sub_total': sub_total,
        }
    else:

        session_cart = request.session.get('cart', {})
        cart_list = []

        for pid, qty in session_cart.items():
            try:
                product = Product.objects.get(pid=pid)
                qty = int(qty) 
                cart_item_total = product.price * qty

                cart_list.append({
                    'product': product,
                    'quantity': qty,
                    'total': cart_item_total,
                })
                sub_total += cart_item_total
            except Product.DoesNotExist:
                continue  # If the product doesn't exist, skip it

        context = {
            'cart': cart_list,
            'sub_total': sub_total,
        }

    return render(request, 'cart.html', context)

@receiver(user_logged_in)
def merge_cart(sender,user,request,**kwargs):
    session_cart=request.session.get('cart',{})
    if session_cart:
        for pid,qty in session_cart.items():
            cart=cartmodels.Cart.objects.get_or_create(user=user)

            cart_item=cartmodels.CartItem.objects.filter(cart=cart,product__pid=pid).first()
            if cart_item:
                cart_item.quantity +=int(qty)
                cart_item.save()
            else:
                cartmodels.CartItem.objects.create(
                    cart=cart,
                    product=Product.objects.get(pid=pid),
                    quantity=qty,
                )
        request.session['cart']={}


            

def CartQtyDecrement(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            user=request.user
            pid=request.POST.get('pid')
            print("----------------------",pid)
            
            updated_qty=request.POST.get('updated_qty')
            product=Product.objects.get(pid=pid)

            cart=cartmodels.Cart.objects.get(user=user)

            cart_item=cartmodels.CartItem.objects.filter(cart=cart,product=product).first()
            
            if cart_item:
                cart_item.quantity=updated_qty
                cart_item.save()
                messages.success(request,"quantity updated")
                cart_item=cartmodels.CartItem.objects.filter(cart=cart,product=product).first()
                new_total=cart_item.total()

                cart=cartmodels.CartItem.objects.filter(cart=cart)
                sub_total=0

                for item in cart:
                    sub_total=item.total() + sub_total
                main_cart=cartmodels.Cart.objects.get(user=user)
                main_cart.total_amount=sub_total-main_cart.discount

                main_cart.save()
                return JsonResponse({"message":"quantity updated","new_total":new_total,"sub_total":sub_total})
            else:
                return JsonResponse({"message":"cart item is not present"})
            
        else:
            pid=request.POST.get('pid')
            updated_qty=request.POST.get('updated_qty')
            session_cart=request.session.get('cart',{})
            sub_total=0
            if str(pid) in session_cart:
                session_cart[str(pid)]=updated_qty
                request.session['cart']=session_cart
                product=Product.objects.get(pid=pid)
                new_total=product.price * int(updated_qty)
                
                for pid,qty  in session_cart.items():
                    product=Product.objects.get(pid=pid)
                    qty=int(qty)
                    cart_item_total=product.price * qty
                    sub_total+=cart_item_total
                return JsonResponse({"message":"quantity updated" ,"new_total":new_total,"sub_total":sub_total})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def CartQtyIncrement(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            user=request.user
            pid=request.POST.get('pid')
            print("----------------------",pid)

            updated_qty=request.POST.get('updated_qty')
            product=Product.objects.get(pid=pid)
            cart=cartmodels.Cart.objects.get(user=user)

            cart_item=cartmodels.CartItem.objects.filter(cart=cart,product=product).first()
            
            if cart_item:
                cart_item.quantity=updated_qty
                cart_item.save()
                messages.success(request,"quantity updated")
                cart_item=cartmodels.CartItem.objects.filter(cart=cart,product=product).first()
                new_total=cart_item.total()

                cart=cartmodels.CartItem.objects.filter(cart=cart)
                sub_total=0

                for item in cart:
                    sub_total=item.total() + sub_total
                main_cart=cartmodels.Cart.objects.get(user=user)
                main_cart.total_amount=sub_total-main_cart.discount
                main_cart.save()
                return JsonResponse({"message":"quantity updated","new_total":new_total,"sub_total":sub_total})
            else:
                return JsonResponse({"message":"cart item is not present"})
            
        else:
            pid=request.POST.get('pid')
            updated_qty=request.POST.get('updated_qty')
            session_cart=request.session.get('cart',{})
            sub_total=0
            if str(pid) in session_cart:
                session_cart[str(pid)]=updated_qty
                request.session['cart']=session_cart
                product=Product.objects.get(pid=pid)
                new_total=product.price * int(updated_qty)
                
                for pid,qty  in session_cart.items():
                    product=Product.objects.get(pid=pid)
                    qty=int(qty)
                    cart_item_total=product.price * qty
                    sub_total+=cart_item_total
                return JsonResponse({"message":"quantity updated" ,"new_total":new_total,"sub_total":sub_total})

    return JsonResponse({'error': 'Invalid request'}, status=400)




def removeItem(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            user=request.user
            pid=request.POST.get('pid')

            product=Product.objects.get(pid=pid)
            cart=cartmodels.Cart.objects.get(user=user)
            cart_item=cartmodels.CartItem.objects.filter(cart=cart,product=product).first()
            if cart_item:
                cart_item.delete()
                cart=cartmodels.CartItem.objects.filter(cart=cart)
                sub_total=0
                for item in cart:
                    sub_total=item.total() + sub_total
                main_cart=cartmodels.Cart.objects.get(user=user)
                main_cart.total_amount=sub_total-main_cart.total_amount
                main_cart.save()    
                
                return JsonResponse({"message":"item deleted","sub_total":sub_total})
            
            else:
                return JsonResponse({"message":"item is not exist"})
        else:
            pid=request.POST.get('pid')
            session_cart=request.session.get('cart',{})
            if str(pid) in session_cart:
                del session_cart[str(pid)]
                request.session['cart']=session_cart
                sub_total=0
                for pid,qty in session_cart.items():
                    product=Product.objects.get(pid=pid)
                    new_total=product.price * int(qty)
                    sub_total +=new_total

                return JsonResponse({"message":"item deleted","sub_total":sub_total})

            else:
                return JsonResponse({"message":"item is not exist"})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def wishlistView(request):
    if request.user.is_authenticated:
        wishlist=cartmodels.wishlist.objects.filter(user=request.user)
        return render(request,'wishlist.html',{"wishlist":wishlist})
    

def wishlistAdd(request):
    if request.method=="POST":
        pid=request.POST.get('pid')
        product=Product.objects.get(pid=pid)
        user=request.user
        wishlist_item=cartmodels.wishlist.objects.filter(user=user,product=product).first()
        if wishlist_item:
            # messages.info(request,"product is already in wishlist")
            return JsonResponse({"message":"product is already in wishlist"})
        else:
            cartmodels.wishlist.objects.create(
                user=user,
                product=product,    
            )
            # messages.success(request,"added to wishlist")
            return JsonResponse({"message":"Added to Wishlist"})

    return JsonResponse({'error': 'Invalid request'}, status=400)


def coupon_apply(request):
    if request.method=="POST":
        coupon_code=request.POST.get('coupon_code')
        cart=cartmodels.Cart.objects.get(user=request.user)
        cart_items=cartmodels.CartItem.objects.filter(cart=cart)
        sub_total=cart.total_amount
        print("-----------------------------------------------",sub_total)

        try :
            coupon=cartmodels.Coupon.objects.get(code=coupon_code)
            if coupon.active==True:
                used_by_user=cartmodels.CouponUsed.objects.filter(coupon=coupon,user=request.user).first()

                if not cart.discount ==0.00:
                    messages.error(request,"Coupon is already applied")
                    return JsonResponse({"message":"Coupon is already applied","icon":"error"})
                
                else:

                    if used_by_user:
                        messages.error(request,"Coupon is already used by you")
                        return JsonResponse({"message":"Coupon is already used by you","icon":"error"})
                    else:
                        
                        discount=sub_total * (Decimal(coupon.discount_percentage) / 100)
                        new_sub_total=sub_total - discount
                        cart.total_amount=new_sub_total
                        cart.discount+=discount
                        cart.save()
                        cartmodels.CouponUsed.objects.create(
                            user=request.user,
                            coupon=coupon,
                            discounted_amount=discount
                        )
                        messages.success(request,"Coupon Applied Successfully")
                        return JsonResponse({"message":"Coupon Applied Successfully","icon":"success"})
            else:
                messages.error(request,"Coupon is not valid")
                return JsonResponse({"message":"Coupon is not valid","icon":"error"})
        except cartmodels.Coupon.DoesNotExist:
            messages.error(request,"Coupon is not exist")
            return JsonResponse({"message":"Coupon is not exist","icon":"error"})


    return JsonResponse({'error': 'Invalid request'}, status=400)
    
            


def place_order(request):
    if request.user.is_authenticated:
        user=request.user
        cart=cartmodels.Cart.objects.get(user=user)
        cart_items=cartmodels.CartItem.objects.filter(cart=cart)
        sub_total=0
        for item in cart_items:
            sub_total+=item.total()
            
        grand_total=cart.total_amount
        discount=cart.discount

        # if not discount==0.00:
        #     grand_total=cart.total_amount - discount


        
        context={
            "cart":cart_items,
            "sub_total":sub_total,
            "grand_total":grand_total,
            "saved":discount,
        }

    return render(request,'checkout.html',context)
        
