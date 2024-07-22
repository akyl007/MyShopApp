from PIL.Image import Image
from django.forms import ModelForm, TextInput, ClearableFileInput

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'image']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название продукта'}),
            'price': TextInput(attrs={'class': 'form-control','placeholder': 'Цена продукта'}),
            'description': TextInput(attrs={'class': 'form-control','placeholder': ' Описание'}),
            'image': ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
