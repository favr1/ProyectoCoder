# Generated by Django 4.1.5 on 2023-02-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_remove_piezas_caracteristicas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autos',
            name='rep_mod',
            field=models.CharField(default='', help_text='reparacion o modificacion', max_length=600),
        ),
    ]
