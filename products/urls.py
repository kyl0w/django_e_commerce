
from django.urls import path
from .views import ListProductsView, CreateProductView

urlpatterns = [
    path('', ListProductsView.as_view(), name='product_list'),  # List view
    path('create/', CreateProductView.as_view(), name='create_product'),  # Create view
]