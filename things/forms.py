"""Forms of the project."""

from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    # name = forms.CharField(label='Your name')
    # description = forms.Textarea(label='Description')
    # quantity = forms.NumberInput(label='Quantity')
    class Meta:
        model = Thing
        fields = ['name','description','quantity']