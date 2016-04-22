# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0002_localizacion_localizacion_padre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localizacion',
            name='localizacion_padre',
            field=models.ForeignKey(to='transacciones.Localizacion', blank=True),
        ),
    ]
