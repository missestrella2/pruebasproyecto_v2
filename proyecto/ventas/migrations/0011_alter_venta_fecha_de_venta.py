# Generated by Django 4.1.3 on 2022-12-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_venta_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='fecha_de_venta',
            field=models.DateField(max_length=25, verbose_name='Fecha de Venta'),
        ),
    ]