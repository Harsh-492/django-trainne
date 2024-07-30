from django.urls import path
from .views import ProfileTemplateView,DashborderView,MyDashboard
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('profile/',ProfileTemplateView.as_view()),
    path('dashboard/',DashborderView.as_view()),
    path('dashboard2/',MyDashboard.as_view(),name='mydashboard'),   
    path('login/',LoginView.as_view(template_name='registration/login.html',redirect_field_name='/registration/mydashboard/'),name='login'),
]
