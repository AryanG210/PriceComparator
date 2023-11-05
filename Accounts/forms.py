from django import forms 
from .models import User

class Login_Form(forms.Form):
    email = forms.EmailField(required=True)
    password =  forms.CharField(widget=forms.PasswordInput,max_length=100,required=True)
    
    class Meta:
        model = User

class Register_form(forms.Form):
    username = forms.CharField(max_length=50,label='username',required=True)
    name= forms.CharField(max_length=50,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, label='password',max_length=100,required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='confirm password',max_length=100,required=True)

    def clean_pswd(self):
        if 'password' in self.cleaned_data:
            return self.cleaned_data['password']
    
    def clean_conf_pswd(self):
        if 'confirm_password' in self.cleaned_data:
            return self.cleaned_data['confirm_password']
        
    def clean_name(self):
         if 'name' in self.cleaned_data:
            return self.cleaned_data['name']
         
    def clean_email(self):
        if 'email' in self.cleaned_data:
            return self.cleaned_data['email']
    
    def clean_username(self):
        if 'username' in self.cleaned_data:
            return self.cleaned_data['username']
    
    class Meta:
        model = User
