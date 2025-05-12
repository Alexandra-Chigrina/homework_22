from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from catalog.models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.order_by("-created_at")


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "image", "category", "price"]
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.POST.get("delete_image") and self.object.image:
            self.object.image.delete(save=True)

        return response

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')


class ContactView(View):
    def get(self, request):
        return render(request, "catalog/contacts.html")

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        print("Имя:", name)
        print("Телефон:", phone)
        print("Сообщение:", message)

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
