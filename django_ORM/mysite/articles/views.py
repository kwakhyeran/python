from django.shortcuts import render, redirect
# 모델 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 전체 데이터 가져오기
    articles = Article.objects.all()[::-1]
    # 그 데이터 템플릿에게 넘겨주기
    context = {
        'articles': articles
    }
    # 템플릿에서 반복문으로 각각의 게시글의
    # pk, title 보여주기
    return render(request, 'articles/index.html', 
    context)

def introduce(request):
    return render(request, 'articles/introduce.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터 생성을 위한 ORM 활용
    # 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # aritcle.save()

    # 두번째 방법
    # article = Article(title=title, content=content)
    # aritlce.save()

    Article.objects.create(title=title, content=content)
    # 어떤 방식을 사용 했는가에 따라서
    # save() 메서드를 사용 할 것인지 아닌지 
    # redirect('appname:경로이름')
    return redirect('articles:index')

# 1. 상세페이지를 보기위한 경로
# 1-1. 특정 게시글에 대한 고유 값
# 1-2. /articles/1/, /articles/2/
# /articles/{{article.pk}}/
#{% url 'articles:detail' article.pk %}
# 2. 해당 게시글에 대한 상세 내용
# 2-1. 게시글의 pk, title, ... 
# 3. 인덱스 페이지로 돌아가는 링크

def detail(request,article_pk):
    # render => 사용자에게 보여줄 파일
    # variable routing? => URL 주소자체를 변수로 사용하는것을 의미
    article = Article.objects.get(pk=article_pk)
    context ={
        'article':article,
    }
    return render(request,'articles/detail.html',context)

# 1. 특정 글 삭제를 위한 경로 작성
# 1-1. /articles/1/delete/
# 2. 글 삭제 처리를 해주는 view 작성
# 3. 글 살제 후 , index page로 redirect
# 4. 글 삭제를 위한 링크 detail에 작성
"""
#GET방식일때 
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
"""

# POST방식
def delete(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail',article_pk)

# edit 
# 1. 특정 글 수정을 위한 경로 생성
# 1-1. /articles/1/edit.
# 2. 글 수정 template 를 render하는 edit view 작성
# 2-1. 해당 template에 form tag작성
# 2-2. 각 input tag 내부에 기존 내용이 들어있어야 함
# 2-3. value 속성을 활용 하시면 됩니다.

def edit(request,article_pk):
    article = Article.objects.get(pk = article_pk)
    context ={
        'article':article,
    }
    return render(request,'articles/edit.html',context)


# update
# 3. edit에서 보낸 데이터 처리를 위한 경로 생성
# 3-1 . /articles/1/update/
# 4. 글 수정 처리를 하는 update view 작성
# 5. 해당 글 상세 페이지로 redirect
# 6. 글 수정을 위한 edit 링크 상세 페이지에 생성
# 6-1. {% url 'articles:edit' article.pk %}
"""
#get방식
def update(request,article_pk):
    article = Article.objects.get(pk = article_pk)
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect('articles:detail', article_pk)
    # detail에서 pk를 받기 때문에 redirect에서도 pk를 넘겨준다.

"""

def update(request,article_pk):
    article = Article.objects.get(pk = article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article_pk)
