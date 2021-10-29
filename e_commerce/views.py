from django.shortcuts import render, HttpResponse



def home_page(request):
      template_name = "base2.html"
      return render(request, template_name)
