from django.urls import path
from .views import UserListView,UserDetailView,UserCreateView,UserUpdateView,UserDeleteView
urlpatterns = [
    path('userlist/',UserListView,name = 'userlist'),
    path('userdetail/<int:pk>/',UserDetailView,name='userdetail'),
    path('usercreate/',UserCreateView,name = 'usercreate'),
    path('userupdate/<int:pk>/',UserUpdateView,name = 'userupdate'),
    path('userdelete/<int:pk>/',UserDeleteView,name ='userdelete'),
]
