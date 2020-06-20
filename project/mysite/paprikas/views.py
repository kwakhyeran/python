from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def main(request):
    return render(request,'paprikas/main.html')

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_vaild():
            article = form.save()
            return redirect('paprikas:index')
    else :
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'paprikas/create.html',context)
    
        