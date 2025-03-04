from django import forms
from .models import Product
class productForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=["title","description","price","summary","featured"]
class rawform(forms.Form):
    title=forms.CharField()
    description=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"your description"}))
    price=forms.DecimalField()
    summary=forms.CharField()
    featured=forms.BooleanField()

