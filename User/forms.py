from django.contrib.auth.models import User
from django import forms
from .models import User_extra


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'validate'}),
            'last_name': forms.TextInput(attrs={'class': 'validate'}),
            'username': forms.TextInput(attrs={'class': 'validate'}),
            'email': forms.TextInput(attrs={'class': 'validate'}),
        }


class UserExtraForm(forms.ModelForm):
    class Meta:
        model = User_extra
        fields = ['profile_picture']
        widgets = {
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        exclude = ('user', )
