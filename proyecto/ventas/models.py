from django.db import models

from clientes.models import Cliente
from formasdepago.models import PagoForma

  
class Venta(models.Model):
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagoformas = models.ForeignKey(PagoForma, on_delete=models.CASCADE)
    fecha_de_venta = models.DateField(verbose_name='Fecha de Venta')
    monto = models.IntegerField(default=0,verbose_name='Monto')

