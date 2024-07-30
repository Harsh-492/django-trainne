from django import forms
from .models import MyProject,ProjectModule

class ProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = '__all__'

class ProjectModuleForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'