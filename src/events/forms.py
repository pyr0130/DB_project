from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'password' : forms.PasswordInput(),
        }
        fields = ['email', 'password', 'name', 'sex', 'contact', 'birth','coin']

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		widgets = {
        'password' : forms.PasswordInput(),
        }
		fields = ['email', 'password']
