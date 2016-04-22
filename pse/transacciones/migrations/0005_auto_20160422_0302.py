# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0004_auto_20160422_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacion',
            name='localizacion_padre',
            field=models.ForeignKey(blank=True, to='transacciones.Localizacion', null=True),
        ),
    ]
