from django import forms
from django.forms import ModelForm, CharField
# from .models import BillOfSale
# from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

#Not needed anymore?
class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
