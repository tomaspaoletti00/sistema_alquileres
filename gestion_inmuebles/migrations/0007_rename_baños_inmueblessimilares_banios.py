# Generated by Django 5.2 on 2025-05-17 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0006_rename_precio_inmueble_precio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueblessimilares',
            old_name='baños',
            new_name='banios',
        ),
    ]
