from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.ProductListView.as_view(), name="index"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path(
        "products/<int:pk>/", views.ProductDetailView.as_view(), name="product_details"
    ),
    path("products/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "products/update/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "products/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
