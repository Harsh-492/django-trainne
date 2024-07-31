from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators


def in_special(value):
 count = 0
 for i in value:
  if count == 0:
   if i.isalnum():
    count +=1
 if count ==0:
  raise forms.ValidationError("username must contain only alphanumeric characters")
 
  

class SignUpForm(UserCreationForm):
 password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
 first_name = forms.CharField(validators=[validators.MaxLengthValidator(5)])
 username = forms.CharField(validators=[in_special])    
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email']
  labels = {'email': 'Email'}

class EditUserProfileForm(UserChangeForm):
 password = None
 class Meta:
  model = User
  fields = ['username', 'first_name', 'last_name', 'email', 'date_joined', 'last_login']
  labels = {'email': 'Email'}

class EditAdminProfileForm(UserChangeForm):
 password = None
 class Meta:
  model = User
  fields = '__all__'
  labels = {'email': 'Email'}
