from .models import *
from django.db.models import Q
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.contrib.auth.decorators import login_required





# returns lists of all categories
def categories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return context


# returns lists of all available products
def product_list(request):
    template_name = "ecommerceapp/product_list.html"
    products = Product.objects.filter(available=True)
    context = {"products": products}
    return render(request, template_name, context)


# returns details of each product
def product_detail(request, slug):
    template_name = "ecommerceapp/product_detail.html"
    product = get_object_or_404(Product, slug=slug)
    context = {"product": product}
    return render(request, template_name, context)


#filter, fetches and returns all products associated with specific categories
def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    template_name = "ecommerceapp/list_by_category.html"
    context = {"category": category, "products": products}
    return render(request, template_name, context)


# fetches products by category, brand and product name
class SearcItem(ListView):
    template_name = "ecommerceapp/product_list.html"
    model = Product
    context_object_name = "products"

    def get_queryset(self):
        query = self.request.GET.get("search")
        if query:
            products = Product.objects.filter(
                Q(name__icontains=query, available=True) | 
                Q(brand_name__icontains=query, available=True) |
                Q(category__name__icontains=query, available=True)
            )
            return products
        return None