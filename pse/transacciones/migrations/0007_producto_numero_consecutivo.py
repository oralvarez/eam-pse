# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-27 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0006_auto_20160425_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='numero_consecutivo',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=30),
            preserve_default=False,
        ),
    ]