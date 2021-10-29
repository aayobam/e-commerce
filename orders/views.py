from django.shortcuts import render


def order_success(request):
      template_name = "payment/orderplaced.html"
      return render(request, template_name)


def orders_view(request):
      template_name = "orders/orders.html"
      context = {"message": "your order histories are displayed here"}
      return render(request, template_name, context)
