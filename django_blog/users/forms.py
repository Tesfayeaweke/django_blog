from django.contrib.auth.forms import UserCreationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.contrib.auth.models import User

class MyCustomForm(UserCreationForm):
    # def __init__(self ,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('username', placeholder = 'Enter your username'),
    #         Field('first_name', placeholder = 'Enter your firstname'),
    #         Field('last_name', placeholder = 'Enter your lastname'),
    #         Field('email', placeholder = 'name@example.com'),
    #         Field('password1', placeholder = 'enter password'),
    #         Field('password2', placeholder = 'confirm password'),
    #     )
        
            

    
    
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

        # widgets  = {'username': forms.TextInput(attrs={'class': 'form-control', 
        #                 'placeholder': 'username'}),
        #             'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'name@example.com'}),
        #             'first_name': forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),
        #             'password1': forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),
        #             'password2': forms.PasswordInput(attrs={'class':'form-control','placeholder':'confirm password'}),
        #             }