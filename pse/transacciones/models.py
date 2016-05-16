from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.db.models import Max
from django.template.loader import render_to_string
from django.contrib.auth.models import User, Permission
from django.db.models import Q

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
        return '%s - %s' % (self.id, self.nombre)

class TipoObjeto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __unicode__(self):
        return '%s - %s' % (self.id, self.nombre)


class TipoProducto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __unicode__(self):
        return '%s - %s' %(self.id, self.nombre)

def content_file_name(instance, filename):
    return '/'.join(['clientes', instance.nit, filename])

def content_file_name_anexo(instance, filename):
    return '/'.join(['anexos', instance.producto, filename])

class Cliente(models.Model):
    nit = models.CharField(max_length=50)
    razon_social = models.TextField()
    direccion = models.CharField(max_length=200)
    ciudad = models.ForeignKey(Ciudad)
    telefono = models.CharField(max_length=50)
    datos_contacto = models.CharField(max_length=200)
    logo = models.FileField(upload_to=content_file_name, max_length=500)

    def __unicode__(self):
        return '%s - %s' %(self.nit, self.razon_social)

class Localizacion(models.Model):
    cliente = models.ForeignKey(Cliente)
    identificacion = models.CharField(max_length=50)
    nombre = models.TextField()
    codigo = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoObjeto)
    centro_costo = models.CharField(max_length=50)
    localizacion_padre = models.ForeignKey('self', null=True, blank=True)
    
    def __unicode__(self):
        return 'CLIENTE: %s - IDENTIFICACION: %s - TIPO: %s - NOMBRE: %s' % (self.cliente, self.identificacion, self.tipo, self.nombre)

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

class Anexo_Producto(models.Model):
    producto = models.ForeignKey(Producto)
    usuario = models.ForeignKey(User)
    anexo = models.FileField(upload_to='anexos')
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s - %s - %s - %s' % (self.producto, self.usuario, self.anexo, self.fecha)

class Estado_Producto(models.Model):
    producto = models.ForeignKey(Producto)
    usuario = models.ForeignKey(User)
    estado_anterior = models.CharField(max_length=100, blank=True, null=True)
    accion = models.CharField(max_length=100, blank=True, null=True)
    estado_actual = models.CharField(max_length=100, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s - %s - %s - %s - %s - %s - %s' % (self.producto, self.usuario, self.estado_anterior, self.accion, self.estado_actual, self.fecha, self.descripcion)


class Usuario_Localizacion(models.Model):
    localizacion = models.ForeignKey(Localizacion)
    usuario = models.ForeignKey(User)
    vigencia_fecha_desde = models.DateField()
    vigencia_fecha_hasta = models.DateField()

    def __unicode__(self):
        return '%s - %s - %s - %s' % (self.localizacion, self.usuario, self.vigencia_fecha_desde, self.vigencia_fecha_hasta)

class Acciones_Estado(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.descripcion)

class Acciones_Sourcing(models.Model):
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.descripcion)

@receiver(post_save, sender=Producto)
def enviar_notificacion_actualizacion_producto(sender, instance, created, *args, **kwargs):
    from_message = "oralvarez@gmail.com"
    #instance.usuario = request.user
    nombre_usuario = instance.usuario.username #User.objects.get(username=instance.usuario.username).first_name + " " + User.objects.get(username=instance.usuario.username).last_name
    to_message = User.objects.get(username=instance.usuario.username).email
    subject = "Probando"
    message = "Probando"

    recipients = []
    for user in User.objects.filter(groups__name='Asignador'):
        recipients.append(user.email)

    for user in User.objects.filter(groups__name='Administradores'):
        recipients.append(user.email)

    if created:
        instance.numero_consecutivo = Producto.objects.all().aggregate(Max('numero_consecutivo')).get('numero_consecutivo__max') + 1
        instance.consecutivo = "ASD-2016-" + str(instance.numero_consecutivo)
        instance.estado = "Sin Asignar"
        ep = Estado_Producto(producto=instance, usuario=instance.usuario, estado_anterior="", accion="Crear", estado_actual="Sin Asignar", descripcion="Creacion de servicio con ID: " + instance.consecutivo)
        ep.save()
        instance.save()
        subject = "Actividad: " + str(instance.consecutivo) + " creada"
        message = render_to_string('tema3/correo.html', {'usuario': nombre_usuario, 'consecutivo': instance.consecutivo})
    else:
         subject = "Actividad: " + str(instance.consecutivo) + " actualizada"
         message = render_to_string('tema3/correo.html', {'usuario': nombre_usuario, 'consecutivo': instance.consecutivo})

    send_mail(subject, message, from_message, [to_message], fail_silently=False, html_message=message)
    #send_mail(subject, message, from_message, [recipients], fail_silently=False, html_message=message)

@receiver(post_delete, sender=Producto)
def enviar_notificacion_borrado_producto(sender, instance, *args, **kwargs):
    from_message = "oralvarez@gmail.com"
    to_message = User.objects.get(username=instance.usuario.username).email
    subject = "Actividad: " + str(instance.consecutivo) + " borrada"
    message = "Se ha borrado la actividad # " + str(instance.consecutivo) + ", por favor verificar"

    # recipients = []
    # for ep in Estado_Producto.objects.get()
    # for user in User.objects.filter(groups__name='Asignador'):
    #     recipients.append(user.email)

    send_mail(subject, message, from_message, [to_message], fail_silently=False)
    #send_mail(subject, message, from_message, [recipients], fail_silently=False, html_message=message)

@receiver(post_save, sender=Estado_Producto)
def enviar_notificacion_actualizacion_estado_producto(sender, instance, created, *args, **kwargs):
    from_message = "oralvarez@gmail.com"
    #instance.usuario = request.user
    nombre_usuario = instance.usuario.username #User.objects.get(username=instance.usuario.username).first_name + " " + User.objects.get(username=instance.usuario.username).last_name
    to_message = User.objects.get(username=instance.usuario.username).email

    s_accion = Acciones_Estado.objects.get(pk=int(instance.accion))
    s_estado_actual = ""

    if s_accion.descripcion == "Asignar":
        s_estado_actual = "Asignado"

    if s_accion.descripcion == "Devolver":
        s_estado_actual = "Devuelto"

    if s_accion.descripcion == "Cerrar":
        s_estado_actual = "Cerrado"

    if s_accion.descripcion == "Cancelar":
        s_estado_actual = "Cancelado"

    recipients = []
    for user in User.objects.filter(groups__name='Asignador'):
        recipients.append(user.email)

    for user in User.objects.filter(groups__name='Administradores'):
        recipients.append(user.email)

    p = Producto.objects.get(pk=instance.producto.id)

    instance.estado_anterior = p.estado
    p.estado = s_estado_actual
    p.save()

    instance.save()

    subject = "Accion realizada en Servicio: " + str(p.consecutivo) + " "
    message = render_to_string('tema3/correo.html', {'usuario': nombre_usuario, 'consecutivo': p.consecutivo})

    send_mail(subject, message, from_message, [to_message], fail_silently=False, html_message=message)
    #send_mail(subject, message, from_message, [recipients], fail_silently=False, html_message=message)
