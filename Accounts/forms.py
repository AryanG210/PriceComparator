from django import forms 
from .models import User

class Login_Form(forms.Form):
    email = forms.EmailField(required=True)
    password =  forms.CharField(widget=forms.PasswordInput,max_length=100,required=True)
    
    class Meta:
        model = User

class Register_form(forms.Form):
    name = forms.CharField(max_length=50,label='First Name',required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='password',max_length=100,required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='confirm password',max_length=100,required=True)

    class Meta:
        model = User
