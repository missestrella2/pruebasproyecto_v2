from django.db import models


class PagoForma(models.Model):
    nombre = models.CharField(max_length=100, default=" ", verbose_name='Forma de Pago')
