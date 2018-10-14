from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm (UserCreationForm):
    email=forms.EmailField()

    class Meta:
        # handles configuration
        # model to which data will be stored
        model=User
        # fields on the form
        fields=['username', 'email','password1','password2']
     