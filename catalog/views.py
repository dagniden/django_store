from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"
    paginate_by = 3


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"


class ContactsView(TemplateView):
    template_name = "contacts.html"


# def contacts(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         message = request.POST.get("message")
#         print(f"Получено сообщение от {name} ({phone}): {message}")
#         return HttpResponse("Сообщение успешно отправлено!")
#
#     return render(request, "contacts.html")
