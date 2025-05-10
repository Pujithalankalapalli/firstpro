from django.shortcuts import render
from django.http import HttpResponse
def product_list(request):
    products = [
        {"name": "Apple"},
        {"name": "Oppo"},
        {"name": "Realme"},
        {"name": "Samsung"},
    ]
    return render(request, 'products/index.html', {'products': products})

def dp(request, name):
    product_messages = {
        "Apple": "It is very expensive nd is very expensive",
        "Oppo": "It is very expensive",
        "Realme": "It has quality camera",
        "Samsung": "It has many features"
    }
    msg = product_messages.get(name, "Product not found")
    return HttpResponse(msg)


    

    



