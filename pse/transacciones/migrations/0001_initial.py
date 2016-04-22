# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nit', models.CharField(max_length=50)),
                ('razon_social', models.CharField(max_length=500)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=50)),
                ('datos_contacto', models.CharField(max_length=200)),
                ('logo', models.FileField(max_length=500, upload_to=None)),
                ('ciudad', models.ForeignKey(to='transacciones.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identificacion', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=500)),
                ('codigo', models.CharField(max_length=20)),
                ('centro_costo', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(to='transacciones.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
                ('codigo_iso', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('consecutivo', models.CharField(max_length=30)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('estado', models.CharField(max_length=50)),
                ('fecha_requerido', models.DateField(auto_now_add=True)),
                ('es_secreto', models.BooleanField()),
                ('objeto', models.CharField(max_length=500)),
                ('observaciones', models.CharField(max_length=500)),
                ('numero_proceso', models.CharField(max_length=30)),
                ('nivel_inteligencia', models.CharField(max_length=30)),
                ('descripcion_bien_servicio', models.CharField(max_length=500)),
                ('proveedores_sugeridos', models.CharField(max_length=500)),
                ('numero_contrato', models.CharField(max_length=30)),
                ('numero_requerimiento', models.CharField(max_length=30)),
                ('valor', models.DecimalField(max_digits=20, decimal_places=2)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('fecha_terminacion', models.DateField(auto_now_add=True)),
                ('numero_contrato_marco', models.CharField(max_length=30)),
                ('tipo_contrato_cual', models.CharField(max_length=50)),
                ('numero_pedido_ot_od_os', models.CharField(max_length=50)),
                ('numero_orden_compra', models.CharField(max_length=50)),
                ('nit', models.CharField(max_length=20)),
                ('razon_social', models.CharField(max_length=200)),
                ('localizacion', models.ForeignKey(to='transacciones.Localizacion')),
                ('moneda', models.ForeignKey(to='transacciones.Moneda')),
            ],
        ),
        migrations.CreateModel(
            name='TipoContrato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TipoObjeto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUbicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_contrato',
            field=models.ForeignKey(to='transacciones.TipoContrato'),
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo_ubicacion',
            field=models.ForeignKey(to='transacciones.TipoUbicacion'),
        ),
        migrations.AddField(
            model_name='producto',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='moneda',
            name='pais',
            field=models.ForeignKey(to='transacciones.Pais'),
        ),
        migrations.AddField(
            model_name='localizacion',
            name='tipo',
            field=models.ForeignKey(to='transacciones.TipoObjeto'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(to='transacciones.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(to='transacciones.Departamento'),
        ),
    ]
