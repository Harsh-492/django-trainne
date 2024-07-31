from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView, UpdateView, DeleteView,View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Post
from .forms import SignupForm, LoginForm, PostForm
from django.contrib.auth.models import Group

class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'blog/about.html'

class ContactView(TemplateView):
    template_name = 'blog/contact.html'

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        user = self.request.user
        context['full_name'] = user.get_full_name()
        context['groups'] = user.groups.all()
        context['ip'] = self.request.session.get('ip', 0)
        return context

class SignupView(FormView):
    template_name = 'blog/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful signup

    def form_valid(self, form):
        messages.success(self.request, 'Congratulations! You have become an Author !!!')
        user = form.save()
        group = Group.objects.get(name='Author')
        user.groups.add(group)
        return super().form_valid(form)

class UserLoginView(FormView):
    template_name = 'blog/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        un = form.cleaned_data['username']
        pw = form.cleaned_data['password']
        user = authenticate(username=un, password=pw)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, "Logged in successfully !!!")
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_authenticated:
            return reverse_lazy('dashboard')
        return super().get_success_url()

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/user_login/')

class AddPostView(LoginRequiredMixin, FormView):
    template_name = 'blog/addpost.html'
    form_class = PostForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        Post.objects.create(title=title, description=description)
        return super().form_valid(form)

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/updatepost.html'
    success_url = reverse_lazy('dashboard')

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('dashboard')
