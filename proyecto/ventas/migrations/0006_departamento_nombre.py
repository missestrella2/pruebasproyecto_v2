# Generated by Django 4.1.3 on 2022-12-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_remove_departamento_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='departamento',
            name='nombre',
            field=models.CharField(choices=[('1', 'seccionferreteria'), ('2', 'seccionbazar'), ('3', 'seccioncalzado')], default='1', max_length=1),
        ),
    ]
