# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import Registration
from django import forms
from django.contrib.auth.models import User
 


# inherit user creation form to registrTION FORM
class RegistrationForm(UserCreationForm):
    fullname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Enter your fullname'}))
    phonenumber = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Enter your phonenumber'}))
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']      
 
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter your password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Enter your Confirm password'
        