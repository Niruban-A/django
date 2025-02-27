from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import productForm


# Create your views here.
def home_page(request):
    return render(request,"index.html",{"name":"niruban","my_list":[1,2,3,4,5,"niruban"]})
def  about(request):
    return render(request,"about.html",{})
def data_from_model(request):
    obj=Product.objects.get(id=1)
    context={"title":obj.title,
             "description":obj.description}
    return render(request,"about.html",context)
def enterdata(request):
    form=productForm(request.POST or None)
    if form.is_valid:
        form.save
        form=productForm()
    context={"form":form

    }
    return render(request,"create.html",context)