# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-10 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0003_auto_20160509_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='dummy',
            new_name='comentarios',
        ),
    ]