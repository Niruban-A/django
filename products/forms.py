from django import forms
from .models import Product
class productForm(forms.ModelForm):
    title=forms.CharField()
    class Meta:
        model=Product
        fields=["title","description","price","summary","featured"]
class rawform(forms.Form):
    title=forms.CharField()
    description=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"your description"}))
    price=forms.DecimalField()
    summary=forms.CharField()
    featured=forms.BooleanField()
    def clean_title(self,*args, **kwargs):
        title=self.cleaned_data.get("title")
        if "cfe" in title:
            return title
        else:
            raise forms.ValidationError("this is not a valid title")
