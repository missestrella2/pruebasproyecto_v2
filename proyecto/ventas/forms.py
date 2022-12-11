from django import forms
from django.forms import ValidationError
from .models import Venta
#from .models import Cargo


class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        widgets = {
        'fecha_de_venta': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Elegir fecha', 'type':'date'}),
        }

class AltaVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'

class BuscarVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('fecha_de_venta',)
