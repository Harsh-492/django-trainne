from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from .forms import UserRegisterForm, UserLoginForm, UserPasswordResetForm, UserSetPasswordForm, UserPasswordChangeForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class UserRegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'

class UserPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    form_class = UserPasswordResetForm
    success_url = reverse_lazy('password_reset_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = UserSetPasswordForm
    success_url = reverse_lazy('password_reset_complete')

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


# @method_decorator(login_required, name='dispatch') this is not standard way ,LoginRequiredMixin is started way 
class UserPasswordChangeView(LoginRequiredMixin,PasswordChangeView):
    template_name = 'registration/password_change.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('password_change_done')


# @method_decorator(login_required, name='dispatch')
class UserPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
