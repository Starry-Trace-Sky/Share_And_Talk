from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    nickName = forms.CharField(max_length=20)

    class Meta:
        model = Profile
        fields = ['nickName', 'username', 'password1', 'password2']
        labels = {'nickName': '', 'username': '', 'password1':'', 'password2':''}
