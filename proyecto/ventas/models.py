from django.db import models
from clientes.models import Cliente
from formasdepago.models import PagoForma
#from django_utils.choices import Choice, Choices
#from djchoices import DjangoChoices, ChoiceItem

class Departamento(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre del Dpto',default='')
    
    # no funcionó
    # nombre=models.CharField(max_length=50,choices=DPTOS_CHOICES,default='1'),
    
    #CON DJANGOCHOICES Y DJANGOUTILS2(no funcionó)
            # class Departamento(DjangoChoices):
            #     class DTO(Choices):
            #         seccionferreteria = ChoiceItem("1")
            #         seccionbazar = ChoiceItem("2")
            #         seccioncalzado = ChoiceItem("3")

            # # Fields
            #     nombre = models.CharField(max_length=1, choices=DTO.choices,default=DTO.seccionferreteria)

  
class Venta(models.Model):
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE,verbose_name='ID del cliente')
    pagoformas = models.ForeignKey(PagoForma, on_delete=models.CASCADE, verbose_name='ID de la Forma de Pago')
    departamentos = models.ManyToManyField(Departamento, verbose_name='ID del Departamento')
    fecha_de_venta = models.DateField(verbose_name='Fecha de Venta')
    monto = models.IntegerField(default=0,verbose_name='Monto')

