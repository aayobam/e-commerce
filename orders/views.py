from django.shortcuts import render
from orders.models import *



def order_success(request):
      template_name = "payment/orderplaced.html"
      return render(request, template_name)


def orders_view(request):
      template_name = "orders/orders.html"
      ordered_item = OrderItem.objects.all()
      context = {"orders":ordered_item}
      return render(request, template_name, context)
