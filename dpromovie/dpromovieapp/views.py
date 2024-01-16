from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform
# Create your views here.
def index(request):
    mov=movie.objects.all()
    # context={
    #     'movie_list':mov
    # }
    return render(request,'index.html',{'movie_list':mov})
def detail(request,movie_id):
    obj=movie.objects.get(id=movie_id)

    return render(request,'detail.html',{'movie':obj})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        des=request.POST.get('des')
        year=request.POST.get('year')
        img=request.FILES['img']
        mov=movie(name=name,des=des,year=year,img=img)
        mov.save()
    return render(request,'add.html')
def update(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    form=movieform(request.POST or None, request.FILES,instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':mov})
def delete(request,movie_id):
    if request.method == 'POST':
        mov=movie.objects.get(id=movie_id)
        mov.delete()
        return redirect('/')
    return render(request,'delete.html')

