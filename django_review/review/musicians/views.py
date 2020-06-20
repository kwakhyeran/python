from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
# Create your views here.
def index(request):
    return render(request,'musicians/index.html')

def create(request):
    if request.method=="POST":
        form = MusicianForm(request.POST)
        if form.is_valid():
            #forms를 상속받았기 때문에 사용가능
            # Musician이 models에게 받은 메소드
            # ModelForm  class Meta : model  = Musician을 담아줬다.
            musician = form.save()
            return redirect('musicians:index')
    else :
        form = MusicianForm()
    context = {
        'form' : form
    }
    return render(request,'musicians/create.html',context)

def detail(request,musician_pk):
    musician = Musician.objects.get(pk =musician_pk)
    context ={
        'musician' : musician
    }
    return render(request,'musicians/detail.html',context)

def index(request):
    musicians = Musician.objects.all()
    context = {
        'musicians' : musicians
    }
    return render(request,'musicians/index.html',context)

def update(request,musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method =="POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect('musicians:detail',musician.pk)
    else :
        form = MusicianForm(instance=musician)
    context ={
        'form' : form
    }   
    return render(request,'musicians/create.html',context)

def delete(request,musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    if request.method=="POST":
        musician.delete()
        return redirect('musicians:index')
    return redirect('musicians:detail',musician.pk)
    
    

