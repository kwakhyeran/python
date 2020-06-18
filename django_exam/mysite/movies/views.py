from django.shortcuts import render
from .models import Movie
from .forms import MovieForm
# Create your views here.
def index(request):
   movies = Movie.objects.all()
   context = {
       'movies' : movies
   }
   return render(request,'index/',context)

def detail(request,movie_pk):
    movie = Movie.objects.get(pk = movie_pk)
    context = {
        'movie':movie
    }
    return render(request,'movies/detail.html',context)

def edit(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    if request.method=='POST':
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:movies')
    else :
        form = MovieForm(instance=movie)
    context = {
        'form' : form
    }
    return render(request,'movies:edit.html',context)
