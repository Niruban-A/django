from django.shortcuts import render
from .forms import blog_Forms
from .models import Article

# Create your views here.
def form_display(request):
    form=blog_Forms(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        Article.objects.create(**form.cleaned_data)

        form=blog_Forms()
        
        

    context={"forms":form}
    return render(request,"article_list.html",context)