# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-29 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_auto_20160528_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=30),
        ),
    ]
