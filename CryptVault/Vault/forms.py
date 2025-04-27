from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control','placeholder':'username'
        })
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class RegistrationForm(UserCreationForm):
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))

    class Meta:
        model=User
        fields=['username','email','password']