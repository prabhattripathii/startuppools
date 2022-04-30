from dataclasses import field
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.validators import RegexValidator


class UserRegistrationForm(UserCreationForm):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{10}$', message="Phone number must be entered in the format: '999999999'. Up to 10 digits allowed.")
    phone = forms.CharField(validators=[phone_regex], max_length=12)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password1','password2','phone']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input--style-5',}),
            'first_name': forms.TextInput(attrs={'class': 'input--style-5',}),
            'last_name': forms.TextInput(attrs={'class': 'input--style-5',}),   
            # 'password1': forms.TextInput(attrs={'class': 'input--style-5','type':'password'}),
            'password1': forms.PasswordInput(attrs={'class':'input--style-5'})
            # 'password2': forms.PasswordInput(attrs={'class': 'input--style-5'}),
            # 'phone': forms.TextInput(attrs={'class': 'input--style-5',}),
        }
