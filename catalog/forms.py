from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product

BLOCK_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите категорию"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name").lower()
        for keyword in BLOCK_WORDS:
            if keyword in name:
                self.add_error(
                    "name", "В название продукта не должно быть запрещенных слов"
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description").lower()
        for keyword in BLOCK_WORDS:
            if keyword in description:
                self.add_error(
                    "description", "В описании продукта не должно быть запрещенных слов"
                )
        return description

    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise ValidationError(f"Цена товара должна быть положительной: {value}")

    def clean_price(self):
        price = self.cleaned_data.get("price")
        self.validate_price(price)
        return price
