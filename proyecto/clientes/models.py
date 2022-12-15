from django.db import models

from formasdepago.models import PagoForma


class Cliente(models.Model):
    nombre = models.CharField(max_length=100, default=" ",verbose_name='Nombre')
    apellido = models.CharField(max_length=100, default=" ", verbose_name='Apellido')
    email = models.EmailField(max_length=150, verbose_name='Email')

    def __str__(self):
        return self.nombre + " " + self.apellido

# class FormaDePagoCliente(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     metodo = models.ForeignKey(PagoForma, on_delete=models.CASCADE)
