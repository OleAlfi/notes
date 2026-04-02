from django import forms
from .models import Category, Notes

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["title"]

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "text", "reminder", "category"]
