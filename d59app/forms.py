from django import forms 
from .models import Add

class Registartion(forms.ModelForm):
    class Meta:
        model=Add
        fields=['name','email','password']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
        labels={'name':'Enter the name','email':'Enter the email','password':'Enter the password'}
        name=forms.CharField(error_messages={'required':'Enter Your name'})