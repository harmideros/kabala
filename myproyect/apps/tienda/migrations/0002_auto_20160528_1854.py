# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-28 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='talla',
            field=models.CharField(choices=[('XS', 'small'), ('S', 'small'), ('M', 'medium'), ('L', 'large'), ('XL', 'big')], max_length=2),
        ),
    ]
