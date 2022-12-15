# Generated by Django 4.1.3 on 2022-12-15 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formasdepago', '0001_initial'),
        ('clientes', '0003_delete_formadepagocliente'),
        ('ventas', '0008_departamento_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='clientes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='departamentos',
            field=models.ManyToManyField(to='ventas.departamento', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='pagoformas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formasdepago.pagoforma', verbose_name='Forma de Pago'),
        ),
    ]
