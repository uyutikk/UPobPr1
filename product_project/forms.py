from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        
        fields = ['name', 'slug', 'category', 'description', 'price', 'image', 'stock', 'is_available']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: vana-tallinn-05'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание товара...'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Количество на складе'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }