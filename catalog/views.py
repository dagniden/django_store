from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    queryset = Product.objects.filter(published=True)
    template_name = "index.html"
    context_object_name = "products"
    paginate_by = 20


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    form_class = ProductForm
    context_object_name = "product"
    pk_url_kwarg = "pk"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("catalog:index")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("catalog:index")

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("catalog:index")

    def test_func(self):
        product = self.get_object()
        user = self.request.user
        # Удалять может владелец или модератор (пользователь с правом delete_product)
        return product.owner == user or user.has_perm("catalog.delete_product")


class ContactsView(TemplateView):
    template_name = "contacts.html"
