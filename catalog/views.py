from django.shortcuts import render, HttpResponse, get_object_or_404

from catalog.models import Product


# Create your views here.


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"Получено сообщение от {name} ({phone}): {message}")
        return HttpResponse("Сообщение успешно отправлено!")

    return render(request, "contacts.html")


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, "product_detail.html", context=context)


def index(request):
    context = {'products': Product.objects.all()}
    return render(request, "index.html", context=context)
