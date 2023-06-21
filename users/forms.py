from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    nickname = forms.CharField(max_length=20)

    class Meta:
        model = Profile
        fields = ['nickname', 'username', 'password1', 'password2']
        labels = {'nickname': '', 'username': '', 'password1':'', 'password2':''}
