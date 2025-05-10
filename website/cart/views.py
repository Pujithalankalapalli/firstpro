# Create your views here.
from django.shortcuts import render

def cart(request):
    cart_items = [
        {"name": "Product 1", "quantity": 1, "price": 100},
    ]
    return render(request, 'cart/index.html', {'cart_items': cart_items})