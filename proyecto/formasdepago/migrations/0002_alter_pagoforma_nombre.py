# Generated by Django 4.1.3 on 2022-12-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formasdepago', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagoforma',
            name='nombre',
            field=models.CharField(default=' ', max_length=20, verbose_name='Forma de Pago'),
        ),
    ]