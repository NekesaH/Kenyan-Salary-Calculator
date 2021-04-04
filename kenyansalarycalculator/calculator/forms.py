from django import forms
from django.forms import ModelForm
from .models import Taxes

class TaxesForm(ModelForm):
    class Meta:
        model = Taxes
        
        fields = '__all__'

 