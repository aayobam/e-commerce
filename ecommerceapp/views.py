from django.shortcuts import render, HttpResponse
from .models import *

def project_test_views(request):
    return HttpResponse("<h1>Welcome to sales inventory(e-commerce) landing page</h1>")


def products_view(request):
    
    context = {
        'products': Product.objects.all(), 
    }
    return render(request, 'products/products_list.html', context)