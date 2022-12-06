from django import forms
from django.forms import ValidationError
from ventas.models import PagoForma
#from .models import Cargo

class PagoFormasForm(forms.ModelForm):
    class Meta:
        model = PagoForma
        fields = '__all__'

class AltaPagoFormaForm(forms.ModelForm):
    class Meta:
        model = PagoForma
        fields = ('nombre',)

class BajaPagoFormaForm(forms.ModelForm):
    class Meta:
        model = PagoForma
        fields = '__all__'