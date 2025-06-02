from django import forms
from catalog.models import Product
from django.core.exceptions import ValidationError

forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update({"class": "form-control", "placeholder": "Название продукта"})
        self.fields["description"].widget.attrs.update({"class": "form-control", "placeholder": "Описание продукта"})
        self.fields["category"].widget.attrs.update({"class": "form-control"})
        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите изображение продукта"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Цена продукта в долларах"}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if any(word in name.lower() for word in forbidden_words):
            raise ValidationError("Название не должно содержать запрещенные слова.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        if any(word in description.lower() for word in forbidden_words):
            raise ValidationError("Описание не должно содержать запрещенные слова.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price
