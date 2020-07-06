from django import forms
from .models import Written


class Add(forms.ModelForm):
    class Meta:
        model=Written
        fields=['content']
