from django.urls import path
from .views import CreateProjectView,ListProjectView,UpdateProjectView,DeleteProjectView
urlpatterns = [
    path('createproject/',CreateProjectView.as_view(),name='createproject'),
    path('listproject/',ListProjectView.as_view(),name='listproject'),
    path('updateproject/<int:pk>/',UpdateProjectView.as_view(),name='updateproject'),
    path('deleteproject/<int:pk>/',DeleteProjectView.as_view(),name='deleteproject'),

]
