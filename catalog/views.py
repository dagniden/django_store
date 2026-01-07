from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import HttpResponse, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.forms import ProductForm
from catalog.models import Product


class ProductListView(ListView):
    model = Product
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


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("catalog:index")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    pk_url_kwarg = "pk"
    success_url = reverse_lazy("catalog:index")


class ContactsView(TemplateView):
    template_name = "contacts.html"
