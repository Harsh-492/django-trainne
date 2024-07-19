from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from .forms import UserForm
# Create your views here.
def home(request):
    return HttpResponse("<h1>Home</h1>")

def userdata(request):
    if request.method == 'GET':
        data = User.objects.all()
    return render(request,'userdata.html',{'data':data})

def createdata(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'userform.html',{'form':form})
    else:
        form = UserForm()
        return render(request,'userform.html',{'form':form})

def getdetail(request,pk):
    data = User.objects.get(id=pk)
    print(data)
    return render(request,'userdetail.html',{'data':data})