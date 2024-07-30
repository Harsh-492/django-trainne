from django.urls import path
from .views import book_list,book_create
urlpatterns = [
    path('books/',book_list,name='book_list'),
    path('create/',book_create,name='book_create'),

]
