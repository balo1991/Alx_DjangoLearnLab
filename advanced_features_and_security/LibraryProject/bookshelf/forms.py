# bookshelf/forms.py

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    """
    Form used for creating and editing Book instances.
    Ensures all user input is validated and sanitized.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
