from django import forms
class blog_Forms(forms.Form):
    name=forms.CharField( max_length=120, widget=forms.Textarea(attrs={"placeholder":"you article name"}))
    price=forms.IntegerField()