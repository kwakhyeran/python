from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def main(request):
    return render(request,'paprikas/main.html')

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('paprikas:index')
    else :
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request,'paprikas/create.html',context)

def update(request,paprikas_pk):
    article = Article.objects.get(pk=paprikas_pk)
    #post 방식으로 받을 때  - 수정 
    if request.method == "POST":
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('paprikas:detail',article.pk)
    else :
        form = ArticleForm(instance=article)
    context ={
        'form' : form
    }
    return render(request,'paprikas/create.html',context)

def index(request):
    articles = Article.objects.all()
    context ={
        'articles' : articles
    }
    return render(request, 'paprikas/index.html', context)

def delete(request,paprikas_pk):
    article = Article.objects.get(pk = paprikas_pk)
    if request.method=="POST":
        article.delete()
        return redirect('paprikas:index')
    return redirect('paprikas:detail',article.pk)

def detail(request,paprikas_pk):
    article = Article.objects.get(pk=paprikas_pk)
    context = {
        'article' : article
    }
    return render(request,'paprikas/detail.html',context)
    
        