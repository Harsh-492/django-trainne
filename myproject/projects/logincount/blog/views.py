from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm,LoginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Post
from django.contrib.auth.models import Group
from django.core.cache import cache


# Create your views here.
def home(request):
    post = Post.objects.all()
    print(post)
    return render(request,'blog/home.html',{'post':post})


def about(request):
    return render(request,'blog/about.html')


def contact(request):
    return render(request,'blog/contact.html')



def dashboard(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        print(post)
        print('user : ',user)
        print("Full Name : ",full_name)
        print("GPS : ",gps)
        ip = request.session.get('ip',0)
        ct = cache.get('count',version=user.pk)
        return render(request,'blog/dashboard.html',{'post':post,'full_name':full_name,'groups':gps,'ct':ct})
    else:
        return HttpResponseRedirect('/login/')


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! You  have become a Author !!!')
            user = form.save()
            group = Group.objects.get(name='Author')
            user.groups.add(group)
        return render(request,'blog/signup.html',{'form':form})
    else:
        form = SignupForm()
        return render(request,'blog/signup.html',{'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                un = form.cleaned_data['username']
                pw = form.cleaned_data['password']
                user = authenticate(username=un, password=pw)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in successfully !!!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user_login/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                post = Post(title=title, description=description)
                post.save()
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'blog/addpost.html',{'form':form})
        
    else:
        return HttpResponseRedirect('/login/')
    


def update_post(request,pk):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=pk)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=pk)
            form = PostForm(instance=pi)
        return render(request, 'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')
    

def delete_post(request,id):
    if request.user.is_authenticated:
           if request.method == 'POST':
                pi = Post.objects.get(pk=id)
                pi.delete()
                return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')