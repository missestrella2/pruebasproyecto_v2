# Generated by Django 4.1.3 on 2022-12-15 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_rename_estado_venta_estado_pendiente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='estado_pendiente',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='estado_terminado',
            field=models.BooleanField(default=False),
        ),
    ]
