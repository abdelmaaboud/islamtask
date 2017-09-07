from django.contrib.auth.models import User
from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )
class Register_form(forms.ModelForm):
    username = forms.CharField(label = "USER NAME")
    email = forms.EmailField(label="E-MAIL")
    password = forms.CharField(widget=forms.PasswordInput,label="PASSWORD")
    class Meta:
        model = User
        fields = ['username','email','password']


class Login_form(forms.Form):
    username = forms.CharField(label = "USER NAME")
    password = forms.CharField(widget=forms.PasswordInput,label="PASSWORD")