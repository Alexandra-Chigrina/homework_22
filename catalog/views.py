from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product


class ProductListView(ListView):
    model = Product
    template_name = "catalog/product_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Product.objects.filter(
                Q(status='published') | Q(owner=user)
            ).order_by("-created_at")

        return Product.objects.filter(status='published').order_by("-created_at")


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner =user
        product.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:product_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        if self.request.POST.get("delete_image") and self.object.image:
            self.object.image.delete(save=True)

        return response

    def get_form_class(self):
        product = self.get_object()
        user = self.request.user
        if product.owner == user:
            return ProductForm
        if user.has_perm("catalog.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied("У вас нет прав для редактирования этого продукта.")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:product_list")

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        user = request.user
        if obj.owner != user and not user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Вы не можете удалить этот продукт.")
        return super().dispatch(request, *args, **kwargs)


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
