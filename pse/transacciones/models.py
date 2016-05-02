from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Max

import django
from django.conf import settings
from django.core.mail import send_mail

#Modelos basicos
class Pais(models.Model):
	nombre = models.CharField(max_length=250)
	codigo_iso = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nombre

class Moneda(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()
	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return self.nombre

class Departamento(models.Model):
	nombre = models.CharField(max_length=250)
	pais = models.ForeignKey(Pais)

	def __unicode__(self):
		return self.nombre

class Ciudad(models.Model):
	nombre = models.CharField(max_length=250)
	departamento = models.ForeignKey(Departamento)

	def __unicode__(self):
		return self.nombre
	
class TipoContrato(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

class TipoUbicacion(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __unicode__(self):
		return self.nombre

class TipoObjeto(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

class TipoProducto(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()

	def __unicode__(self):
		return '%s - %s' %(self.id, self.nombre)

def content_file_name(instance, filename):
    return '/'.join(['content', instance.nit, filename])

class Cliente(models.Model):
	nit = models.CharField(max_length=50)
	razon_social = models.TextField()
	direccion = models.CharField(max_length=200)
	ciudad = models.ForeignKey(Ciudad)
	telefono = models.CharField(max_length=50)
	datos_contacto = models.CharField(max_length=200)
	logo = models.FileField(upload_to=content_file_name, max_length=500)

	def __unicode__(self):
		return self.nit

class Localizacion(models.Model):
	cliente = models.ForeignKey(Cliente)
	identificacion = models.CharField(max_length=50)
	nombre = models.TextField()
	codigo = models.CharField(max_length=20)
	tipo = models.ForeignKey(TipoObjeto)
	centro_costo = models.CharField(max_length=50)
	localizacion_padre = models.ForeignKey('self', null=True, blank=True)
	
	def __unicode__(self):
		return self.identificacion

#Modelo principal para todas las transacciones disponibles
class Producto(models.Model):
	consecutivo = models.CharField(max_length=30, blank=True, null=True)
	numero_consecutivo = models.DecimalField(max_digits=30, decimal_places=0, blank=True, null=True)
	fecha_registro = models.DateTimeField(auto_now_add=True, blank=True, null=True, editable=False)
	estado = models.CharField(max_length=50, blank=True, null=True)
	usuario = models.ForeignKey(User, blank=True, null=True)
	fecha_requerido = models.DateField(auto_now_add=True, blank=True, null=True)
	es_secreto = models.NullBooleanField()
	objeto = models.TextField(blank=True, null=True)
	localizacion = models.ForeignKey(Localizacion, blank=True, null=True)
	observaciones = models.TextField(blank=True, null=True)
	numero_proceso = models.CharField(max_length=30, blank=True, null=True)
	nivel_inteligencia = models.CharField(max_length=30, blank=True, null=True)
	descripcion_bien_servicio = models.TextField(blank=True, null=True)
	tipo_ubicacion = models.ForeignKey(TipoUbicacion, blank=True, null=True)
	proveedores_sugeridos = models.TextField(blank=True, null=True)
	numero_contrato = models.CharField(max_length=30, blank=True, null=True)
	numero_requerimiento = models.CharField(max_length=30, blank=True, null=True)
	valor = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
	moneda = models.ForeignKey(Moneda, blank=True, null=True)
	fecha_inicio = models.DateField(blank=True, null=True)
	fecha_terminacion = models.DateField(blank=True, null=True)
	numero_contrato_marco = models.CharField(max_length=30, blank=True, null=True)
	tipo_contrato = models.ForeignKey(TipoContrato, blank=True, null=True)
	tipo_contrato_cual = models.CharField(max_length=50, blank=True, null=True)
	numero_pedido_ot_od_os = models.CharField(max_length=50, blank=True, null=True)
	numero_orden_compra = models.CharField(max_length=50, blank=True, null=True)
	nit = models.CharField(max_length=20, blank=True, null=True)
	razon_social = models.CharField(max_length=200, blank=True, null=True)
	tipo_producto = models.ForeignKey(TipoProducto, blank=True, null=True)
	createdAt =  models.DateTimeField(auto_now_add=True, blank=True, null=True)
	updatedAt = models.DateTimeField(auto_now=True, blank=True, null=True)

	def __unicode__(self):
		return '%s -%s - %s' % (self.consecutivo, self.createdAt, self.updatedAt)

@receiver(post_save, sender=Producto)
def enviar_notificacion_actualizacion_producto(sender, instance, created, *args, **kwargs):
	from_message = "oralvarez@gmail.com"
	to_message = User.objects.get(username=instance.usuario.username).email
	subject = "Probando"
	message = "Probando"

	if created:
		instance.numero_consecutivo = Producto.objects.all().aggregate(Max('numero_consecutivo')).get('numero_consecutivo__max') + 1
		instance.consecutivo = instance.numero_consecutivo
	 	subject = "Actividad: " + str(instance.consecutivo) + " creada"
	 	message = "Se ha creado la actividad # " + str(instance.consecutivo) + ", por favor verificar"
	else:
	 	subject = "Actividad: " + str(instance.consecutivo) + " actualizada"
	 	message = "Se ha actualizado la actividad # " + str(instance.consecutivo) + ", por favor verificar"

	send_mail(subject, message, from_message, [to_message], fail_silently=False)

@receiver(post_delete, sender=Producto)
def enviar_notificacion_borrado_producto(sender, instance, *args, **kwargs):
	from_message = "oralvarez@gmail.com"
	to_message = User.objects.get(username=instance.usuario.username).email
 	subject = "Actividad: " + str(instance.consecutivo) + " borrada"
 	message = "Se ha borrado la actividad # " + str(instance.consecutivo) + ", por favor verificar"

	send_mail(subject, message, from_message, [to_message], fail_silently=False)
