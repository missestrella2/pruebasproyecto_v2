from django import forms
from django.forms import ValidationError
from .models import Venta, Departamento
#from .models import Cargo

############  FORMULARIOS DE VENTAS ########################

class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = '__all__'
        
class AltaVentaForm(forms.ModelForm):
     class Meta:
         model = Venta
         fields = '__all__'
         exclude = ('estado_pendiente','estado_terminado') ###
         #departamentos = forms.MultipleChoiceField()  
         departamentos = forms.CheckboxSelectMultiple()   
         widgets = {
             'fecha_de_venta':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Elegir fecha', 'type':'date'}),
                    }   

#class AltaVentaForm(forms.ModelForm): #no funcionó
    # class Meta:
    #     DPTOS_CHOICES={
    #             ('1','Seccion Bazar'),
    #             ('2','Seccion Ferreteria'),
    #             ('3','Seccion Almacen'),
    #             }
    #     model = Venta
    #     fields = '__all__'
    #     departamentos = forms.ChoiceField(label="Departamento o seccion", choices=DPTOS_CHOICES, initial='3', default='1',required = True,)
    #     widgets = {'fecha_de_venta':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Elegir fecha', 'type':'date'}),
    #                'departamentos': forms.Select(attrs={'class':'form-control'}),
    #     }

class BuscarVentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('fecha_de_venta',)

############  FORMULARIOS DE DEPARTAMENTOS ########################

class DepartamentosForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class AltaDepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

class BajaDepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'