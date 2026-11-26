import requests
from django.shortcuts import render

# Create your views here.

def products(request):
    url = "https://fakestoreapi.com/products"
    response = requests.get(url)
    data = response.json()

    context ={
        "products":data
    }

    return render(request,"products.html",context)