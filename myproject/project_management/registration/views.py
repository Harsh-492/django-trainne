from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

class DashborderView(TemplateView):
    template_name = 'registration/dashboard.html'

class MyDashboard(TemplateView):
    template_name = 'registration/dashboard2.html'   