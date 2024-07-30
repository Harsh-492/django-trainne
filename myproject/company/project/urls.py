from django.urls import path
from .views import CreateProjectView,ListProjectView,UpdateProjectView,DeleteProjectView,CreateProjectModuleView
urlpatterns = [
    path('createproject/',CreateProjectView.as_view(),name='createproject'),
    path('listproject/',ListProjectView.as_view(),name='listproject'),
    path('updateproject/<int:pk>/',UpdateProjectView.as_view(),name='updateproject'),
    path('deleteproject/<int:pk>/',DeleteProjectView.as_view(),name='deleteproject'),
    path('projectmodule/',CreateProjectModuleView.as_view(),name='projectmodule'),

]
