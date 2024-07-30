from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import RedirectView,TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login

class UserRegisterView(FormView):
    template_name = 'registrations/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'registrations/login.html'
    authentication_form = UserLoginForm


    def get_success_url(self):
        return reverse_lazy('profile')



class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ProfileView(TemplateView):
    template_name = 'profile.html'