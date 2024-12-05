from django import forms
from django.contrib.auth.models import User
from .models import EvaluationRequest

from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one number.")
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError("Password must contain at least one letter.")
        return password


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must be at least 8 characters long and contain at least one digit.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class EvaluationRequestForm(forms.ModelForm):
    class Meta:
        model = EvaluationRequest
        fields = ['description', 'contact_method', 'photo']
        labels = {
            'description': 'Item Description',
            'contact_method': 'Preferred Contact Method',
            'photo': 'Upload Photo',
        }