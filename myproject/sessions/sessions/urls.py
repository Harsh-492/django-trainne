"""
URL configuration for sessions project.

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
from student import views
from student1 import views as sv

urlpatterns = [
    path('admin/', admin.site.urls),
     path('set/', views.SetSessionView.as_view(), name='set_session'),
    path('get/', views.GetSessionView.as_view(), name='get_session'),
    path('del/', views.DeleteSessionView.as_view(), name='delete_session'),
    path('setcookie/',sv.settestcookie),
    path('checkcookie/',sv.checktestcookie), 
    path('deletecookie/',sv.deletetestcookie),
]
