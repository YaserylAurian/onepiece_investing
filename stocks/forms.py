from django import forms
from .models import User
class SignUpForm(forms.Form):
    username = forms.CharField(label='username')
    new_password = forms.CharField(label='password', widget=forms.PasswordInput())
    password_confirmation = forms.CharField(label='password confirmation', widget=forms.PasswordInput())