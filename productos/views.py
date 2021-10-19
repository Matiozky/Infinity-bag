from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView
# Create your views here.



class ProductListView(ListView):
    model = Product
    template_name = 'productos/index.html'
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'productos/detail.html'