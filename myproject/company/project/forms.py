from django import forms
from .models import MyProject

class ProjectForm(forms.ModelForm):
    class Meta:
        model = MyProject
        fields = '__all__'