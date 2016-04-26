from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_save
from django.dispatch import receiver

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

	def __unicode__(self):
		return self.nombre

class Cliente(models.Model):
	nit = models.CharField(max_length=50)
	razon_social = models.TextField()
	direccion = models.CharField(max_length=200)
	ciudad = models.ForeignKey(Ciudad)
	telefono = models.CharField(max_length=50)
	datos_contacto = models.CharField(max_length=200)
	logo = models.FileField(upload_to=None, max_length=500)

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
	consecutivo = models.CharField(max_length=30)
	fecha_registro = models.DateField(auto_now_add=True)
	estado = models.CharField(max_length=50)
	usuario = models.ForeignKey(User)
	fecha_requerido = models.DateField(auto_now_add=True)
	es_secreto = models.BooleanField()
	objeto = models.TextField()
	localizacion = models.ForeignKey(Localizacion)
	observaciones = models.TextField()
	numero_proceso = models.CharField(max_length=30)
	nivel_inteligencia = models.CharField(max_length=30)
	descripcion_bien_servicio = models.TextField()
	tipo_ubicacion = models.ForeignKey(TipoUbicacion)
	proveedores_sugeridos = models.TextField()
	numero_contrato = models.CharField(max_length=30)
	numero_requerimiento = models.CharField(max_length=30)
	valor = models.DecimalField(max_digits=20, decimal_places=2)
	moneda = models.ForeignKey(Moneda)
	fecha_inicio = models.DateField()
	fecha_terminacion = models.DateField()
	numero_contrato_marco = models.CharField(max_length=30)
	tipo_contrato = models.ForeignKey(TipoContrato)
	tipo_contrato_cual = models.CharField(max_length=50)
	numero_pedido_ot_od_os = models.CharField(max_length=50)
	numero_orden_compra = models.CharField(max_length=50)
	nit = models.CharField(max_length=20)
	razon_social = models.CharField(max_length=200)

	def __unicode__(self):
		return self.consecutivo

	@receiver(pre_save)
	def my_callback(sender, instance, *args, **kwargs):
    		instance.consecutivo = "100" #Producto.objects.get(pk=1).consecutivo + 1
