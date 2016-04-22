# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transacciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='localizacion',
            name='localizacion_padre',
            field=models.ForeignKey(default=1, to='transacciones.Localizacion'),
            preserve_default=False,
        ),
    ]
