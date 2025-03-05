from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .forms import productForm,rawform


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
    if form.is_valid():
        form.save
        form=productForm()
    context={"form":form

    }
    return render(request,"create.html",context)
def data_from_raw_form(request):
    my_form=rawform()
    if request.method=="POST":
        my_form=rawform(request.POST)
        
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Product.objects.create(**my_form.cleaned_data)
    context={
        "my_forms":my_form
    }
    return render(request,"rawform.html",context)
def dynamic_url_routing (request,my_id):
    obj=Product.objects.get(id=my_id)
    context={
        "objects":obj
    }
    return render(request,"dynamic_rending.html",context)
