# Generated by Django 4.2.1 on 2023-06-03 21:11

import os
from django.db import migrations

def reportesBD():
    sql_script = open(os.path.join('myApp/sql/Inserts.sql'), 'r').read()
    return sql_script


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_alter_detallescompra_id_producto_and_more'),
    ]

    operations = [
        migrations.RunSQL(reportesBD(),)
    ]