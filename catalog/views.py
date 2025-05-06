from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    products = Product.objects.order_by("-created_at")[:5]
    print(products)
    return render(request, "catalog/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print("Имя:", name)
        print("Телефон:", phone)
        print("Сообщение:", message)
        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")

    return render(request, "catalog/contacts.html")


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'catalog/product_detail.html', context)
