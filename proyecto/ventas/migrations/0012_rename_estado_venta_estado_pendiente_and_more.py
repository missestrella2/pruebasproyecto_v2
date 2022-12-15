# Generated by Django 4.1.3 on 2022-12-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0011_alter_venta_fecha_de_venta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='estado',
            new_name='estado_pendiente',
        ),
        migrations.AddField(
            model_name='venta',
            name='estado_terminado',
            field=models.BooleanField(default=True),
        ),
    ]
