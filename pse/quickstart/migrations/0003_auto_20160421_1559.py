# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_remove_nota_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='detalle',
            field=models.CharField(default=datetime.datetime(2016, 4, 21, 15, 58, 39, 501815, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nota',
            name='nombre',
            field=models.CharField(default='EEEE', max_length=100),
            preserve_default=False,
        ),
    ]
