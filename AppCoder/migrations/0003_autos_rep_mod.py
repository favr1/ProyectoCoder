# Generated by Django 4.1.5 on 2023-02-22 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_delete_prueba'),
    ]

    operations = [
        migrations.AddField(
            model_name='autos',
            name='rep_mod',
            field=models.CharField(default='DEFAULT VALUE', help_text='reparacion o modificacion', max_length=600),
        ),
    ]