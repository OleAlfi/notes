from django import forms
from .models import Category, Notes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "text", "reminder", "category"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        ]
