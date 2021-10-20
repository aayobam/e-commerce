from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from ecommerceapp.models import Product
from .cart import Cart
from django.contrib import messages


def cart_summary(request):
    template_name = 'cart/cart_summary.html'
    return render(request, template_name)


def add_to_cart(request):
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart = Cart(request)
        cart.add(product=product, product_qty=product_qty)
        response = JsonResponse({'test':'data'})
        return response