from django.urls import path
from .views import product_list, dp

urlpatterns = [
    path('', product_list, name='products'),
    path('product/<str:name>/', dp, name='product_detail'),  
]
