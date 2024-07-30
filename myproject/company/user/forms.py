from django import forms
from .models import MyUser


class UserForm(forms.ModelForm):

    name = forms.CharField(max_length=7,help_text='Name of the user is less than 7')
    class Meta:
        model = MyUser
        fields = ['name','email','phone','salary','department']