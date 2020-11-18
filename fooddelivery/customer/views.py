from django.shortcuts import render
from django.views import View

# Create your views here.


def Index(request):
    return render(request, 'customer/index.html')


def About(request):
    return render(request, 'customer/about.html')
