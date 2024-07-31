"""
URL configuration for miniblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view()),
    path('about/',views.AboutView.as_view(),name='about'),
    path('contact/',views.ContactView.as_view(),name='contact'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('user_login/',views.UserLoginView.as_view(),name='user_login'),
    path('dashboard/',views.DashboardView.as_view(),name='dashboard'),
    path('user_logout/',views.UserLogoutView.as_view(),name='user_logout'),
    path('addpost/',views.AddPostView.as_view(),name='addpost'),
    path('updatepost/<int:pk>/',views.UpdatePostView.as_view(),name='updatepost'),
    path('deletepost/<int:id>/',views.DeletePostView.as_view(),name='deletepost'),
]
