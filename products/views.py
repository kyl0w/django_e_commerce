from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Products
from .forms import ProductForm

class ListProductsView(ListView):
    model = Products
    template_name = 'manager.html' 
    context_object_name = 'products'

class CreateProductView(CreateView):
    model = Products
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('product_list')