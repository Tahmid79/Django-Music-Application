from django.contrib.auth.models import User
from django import forms
from django.shortcuts import redirect , render
from django.contrib.auth import authenticate, login
from django.views.generic import View

class UserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput)

     class Meta:
        model  = User
        fields = ['username' , 'email' , 'password']




