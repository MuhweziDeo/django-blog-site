from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm (UserCreationForm):
    email=forms.EmailField()

    class Meta:
        # handles configuration
        # model to which data will be stored
        model=User
        # fields on the form
        fields=['username', 'email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        field=['image']
     