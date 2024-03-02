from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'font-size: 20px; background-color: #80E12A; box-shadow: none;',
                    'placeholder': 'write your ID',
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'font-size: 20px; box-shadow: none;',
                    'placeholder': 'write your password',
                }),   
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'font-size: 20px; box-shadow: none;',
                    'placeholder': 'write your e-mail',
                }),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'font-size: 20px; box-shadow: none;',
                    'placeholder': 'write your full name',
                }),    
        }
        
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'font-size: 20px; background-color: #80E12A; box-shadow: none;',
                    'placeholder': 'write your ID',
                }),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control border-0',
                    'style': 'font-size: 20px; box-shadow: none;',
                    'placeholder': 'write your password',
                }),
        }
