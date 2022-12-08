# Generated by Django 4.1.3 on 2022-12-08 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("formasdepago", "0001_initial"),
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormaDePagoCliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.cliente",
                    ),
                ),
                (
                    "metodo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="formasdepago.pagoforma",
                    ),
                ),
            ],
        ),
    ]
