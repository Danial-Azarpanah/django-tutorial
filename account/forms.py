from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"}))

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password", "confirm_password"]
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "first_name": forms.TextInput(attrs={"placeholder": "First Name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last Name"}),
            "password": forms.PasswordInput(attrs={"placeholder": "Password"}),
        }

    def clean(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise ValidationError("گذرواژه و تایید گذرواژه یکسان نیستند")


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )