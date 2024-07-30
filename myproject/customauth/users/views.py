from django.contrib.auth.views import LoginView,LogoutView
from django.shortcuts import redirect, render
from django.views.generic import TemplateView,CreateView,View
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomPasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin




class ProfileView(TemplateView):
        template_name = 'myser/profile.html'


class CustomSignupView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'myser/signup.html'
    success_url = reverse_lazy('login')


class CustomUserLoginView(View):
    template_name = 'myser/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('profile'))  # Replace 'profile' with your profile URL name
        else:
            # Handle invalid login here (e.g., display error message)
            return render(request, self.template_name, {'error': 'Invalid credentials'})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Replace with your login URL

class CustomPasswordChangeView(LoginRequiredMixin,View):
    def get(self, request):
        form = CustomPasswordChangeForm(user=request.user)
        return render(request, 'myser/password_change.html', {'form': form})

    def post(self, request):
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been changed successfully.')
            return redirect('login')  # Replace with your login URL
        return render(request, 'myser/password_change.html', {'form': form})
