from django import forms
from .models import Product
class productForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["title","description","price","summary","featured"]
    
