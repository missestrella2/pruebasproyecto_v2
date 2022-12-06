from django.db import models
from ast import mod
from email.policy import default
from tabnanny import verbose
from django.db import models

class Cliente(models.Model):
    nombre= models.CharField(max_length=100, default=" ",verbose_name='Nombre')
    apellido= models.CharField(max_length=100, default=" ", verbose_name='Apellido')
    email= models.EmailField(max_length=150, verbose_name='Email')

class PagoForma(models.Model):
    nombre= models.CharField(max_length=100, default=" ", verbose_name='Forma de Pago')
    clientes = models.ManyToManyField(Cliente, through = 'Venta')
   
class Venta(models.Model):
    clientes = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pagoformas = models.ForeignKey(PagoForma, on_delete=models.CASCADE)
    fecha_de_venta=models.DateField(verbose_name='Fecha de Venta')
    monto= models.IntegerField(default=0,verbose_name='Monto')

