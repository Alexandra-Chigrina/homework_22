from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from catalog.models import Product, Category


def home(request):
    print(Product.objects.order_by("-created_at")[:5])
    product_list = Product.objects.order_by("-created_at")
    paginator = Paginator(product_list, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj
    }
    return render(request, "catalog/home.html", context)


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


def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        category_id = request.POST.get("category")
        price = request.POST.get("price")

        Product.objects.create(
            name=name,
            description=description,
            image=image,
            category_id=category_id,
            price=price
        )
        return HttpResponse("Товар успешно добавлен!")

    categories = Category.objects.all()
    return render(request, "catalog/add_product.html", {"categories": categories})
