from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from ecommerceapp.models import Product
from .cart import Cart


# holds all product(s) data
def cart_summary(request):
    template_name = 'cart/cart_summary.html'
    cart = Cart(request)
    context = {"cart": cart}
    return render(request, template_name, context)


# adds product(s) to cart
def add_to_cart(request):
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add(product=product, product_qty=product_qty)
        cart_qty = cart.__len__()
        response = JsonResponse({'qty': cart_qty})
        return response


# deletes product(s) from cart
def delete_from_cart(request):
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get("productid"))
        cart = Cart(request)
        cart.delete(product=product_id)
        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({"qty": cart_qty, 'subtotal': cart_total})
        return response


# update product(s) data in cart
def update_cart(request):
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart = Cart(request)
        cart.update(product=product_id, qty=product_qty)
        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({"qty": cart_qty, "subtotal": cart_total})
        return response
