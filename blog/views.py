from django.shortcuts import render,get_object_or_404
from .forms import blog_Forms
from .models import Article
from django.views.generic import ListView ,DetailView

# Create your views here.
def form_display(request):
    form=blog_Forms(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        Article.objects.create(**form.cleaned_data)

        form=blog_Forms()
        
        

    context={"forms":form}
    return render(request,"article_list.html",context)
class Articleclass_view (ListView):
    template_name="article_list.html"
    queryset=Article.objects.all()
class Detailclassview(DetailView):
    template_name="article_detail.html"
    def get_object(self):
        id=self.kwargs.get("id")
        return get_object_or_404(Article,id=id)

