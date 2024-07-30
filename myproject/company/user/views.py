from django.shortcuts import render,redirect,get_object_or_404
from .models import MyUser
from .forms import UserForm
# Create your views here.

def UserListView(request):
    user_data = MyUser.objects.all()
    print(user_data)
    return render(request,'user/user_list.html',{'user_data':user_data})


def UserDetailView(request,pk):
    # user = MyUser.objects.get(id=pk)
    user = get_object_or_404(MyUser, pk=pk)
    print("user : ",user)
    print("Name : ",user.name)
    print('Emial : ',user.email)
    return render(request,'user/user_details.html',{'user':user})

def UserCreateView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            cn = form.cleaned_data['name']
            ce = form.cleaned_data['email']
            cp = form.cleaned_data['phone']
            print("cn : ",cn," ce : ",ce," cp : ",cp)
            form.save()
            return redirect('userlist')
    else :
        form = UserForm()
        return render(request,'user/user_creation.html',{'form':form})

def UserUpdateView(request,pk):
    if request.method == 'POST':
        user = MyUser.objects.get(id=pk)
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
        return redirect('userlist')
    else:

        user = MyUser.objects.get(id=pk)
        form = UserForm(instance=user)
        return render(request, 'user/user_creation.html',{'form':form})
    

def UserDeleteView(request,pk):
    user = MyUser.objects.get(id=pk)
    user.delete()
    return redirect('userlist')
