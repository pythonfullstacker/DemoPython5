from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from .models import Movie
from  .forms import  MovieForm

def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']
        user=auth.authenticate(username=un,password=pw)

        if user is not None:
            auth.login(request,user)
            return redirect('capp:profile')
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        un = request.POST['username']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        mail = request.POST['email']
        pw = request.POST['password']
        cpw = request.POST['password1']

    #     if pw == cpw:
    #         if User.objects.filter(username=un).exists() or User.objects.filter(email=mail).exists():
    #             messages.error(request, 'Username or email already exists.')
    #         else:
    #             user = User.objects.create_user(username=un, email=mail, password=pw, first_name=fn, last_name=ln)
    #             messages.success(request, 'User created successfully.')
    #     else:
    #         messages.error(request, 'Passwords do not match.')
    #
    # return render(request, "register.html")
        if pw == cpw:
           if User.objects.filter(username=un).exists():
                  messages.info(request,"username taken")
                  return redirect('register')
           elif User.objects.filter(email=mail).exists():
                  messages.info(request,"email taken")
                  return redirect('register')
           else:
                  user = User.objects.create_user(username=un,email=mail,password=pw,first_name=fn,last_name=ln)

                  user.save();
                  messages.success(request, "User created successfully.")
                  # return redirect('login')
        else:
          messages.info(request,"password not matching")
          return  redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    movie=Movie.objects.all()
    context={'movie_list':movie
            }

    return render(request, "profile.html",context)

def detail(request,movie_id):
    movie = Movie.objects.get(id=movie_id)

    return render(request, 'detail.html', {'movie': movie})


def add_movie(request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        review_text=request.POST.get(' review_text',)
        link=request.POST.get('link',)
        score = request.POST.get('score',)

        movie=Movie(name=name,desc=desc,year=year,img=img,review_text=review_text,link=link,score=score)
        movie.save()
    return render(request, 'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return  redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})


def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

def home(request):
    return render(request,'index.html')