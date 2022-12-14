# Generated by Django 4.1.3 on 2022-12-08 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("formasdepago", "0001_initial"),
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Venta",
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
                ("fecha_de_venta", models.DateField(verbose_name="Fecha de Venta")),
                ("monto", models.IntegerField(default=0, verbose_name="Monto")),
                (
                    "clientes",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.cliente",
                    ),
                ),
                (
                    "pagoformas",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="formasdepago.pagoforma",
                    ),
                ),
            ],
        ),
    ]
