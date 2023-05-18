from django import forms
from app1.models import ToDo, CustomUser
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.core.exceptions import ValidationError


class AddUserDjangoForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )  

class UpdatedUser(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username"  ,
            "email"     ,
            "first_name",
            "last_name" )


class LogInForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo  
        exclude = ['todo_done', 'count'] 
        widgets = {
            'todo_content' : forms.Textarea(attrs={'cols': 80, 'rows': 10}),
            'todo_date'    : forms.NumberInput(attrs={'type':'date'}),
            'todo_time'    : forms.NumberInput(attrs={'type' : 'time'}),
            'todo_username': forms.HiddenInput()
        }   

class CustoUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ['user']      
