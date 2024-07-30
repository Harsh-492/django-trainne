from django.urls import path
from .views import StudentListView,StudentDetailView,GenreralData,StudentCreateViews,StudentDelete
urlpatterns = [
    path('list/',StudentListView.as_view(),name='list'),
    path('detail/<int:pk>/',StudentDetailView.as_view(),name='detail'),
    path('general/',GenreralData.as_view(),name='general'),
    path('create/',StudentCreateViews.as_view(),name='create'),
    path('delete/',StudentDelete.as_view(),name='delete'),
]
