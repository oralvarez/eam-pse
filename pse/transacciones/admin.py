from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Pais)
admin.site.register(Moneda)
admin.site.register(Departamento)
admin.site.register(Ciudad)
admin.site.register(TipoContrato)
admin.site.register(TipoUbicacion)
admin.site.register(TipoObjeto)
admin.site.register(Cliente)
admin.site.register(Dependencia)
admin.site.register(Usuario_Cliente)

admin.site.register(Anexo_Producto)
admin.site.register(Estado_Producto)
admin.site.register(Acciones_Sourcing)
admin.site.register(Acciones_Estado)
admin.site.register(Detalle_Servicio)

