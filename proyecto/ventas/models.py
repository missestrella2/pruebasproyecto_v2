from django.db import models

from clientes.models import Cliente
from formasdepago.models import PagoForma

class Departamento(models.Model):
    nombre=models.CharField(max_length=100, verbose_name='Nombre del Dpto')

  
class Venta(models.Model):
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE,verbose_name='ID del cliente')
    pagoformas = models.ForeignKey(PagoForma, on_delete=models.CASCADE, verbose_name='ID de la Forma de Pago')
    departamentos = models.ManyToManyField(Departamento, verbose_name='ID del Departamento')
    fecha_de_venta = models.DateField(verbose_name='Fecha de Venta')
    monto = models.IntegerField(default=0,verbose_name='Monto')

