from rest_framework import serializers
from models import Moneda, Pais, Producto, Localizacion, TipoContrato, TipoUbicacion, TipoObjeto, Cliente, TipoProducto 


class MonedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Moneda
        fields = ('id', 'nombre', 'descripcion', 'pais')

class TipoContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoContrato
        fields = ('id', 'nombre', 'descripcion')

class TipoUbicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoUbicacion
        fields = ('id', 'nombre', 'descripcion')

class TipoProducto(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ('id', 'nombre', 'descripcion')

class TipoObjetoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoObjeto
        fields = ('id', 'nombre', 'descripcion')

class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'codigo_iso')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nit', 'razon_social', 'direccion', 'ciudad', 'telefono', 'datos_contacto', 'logo')

class LocalizacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localizacion
        fields = ('id', 'cliente', 'identificacion', 'nombre', 'codigo', 'tipo', 'centro_costo', 'localizacion_padre')
 

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id', 'consecutivo', 'fecha_registro', 'estado', 'usuario', 'fecha_requerido', 'es_secreto', 'objeto', 'localizacion', 'observaciones', 'numero_proceso', 'nivel_inteligencia', 'descripcion_bien_servicio', 'tipo_ubicacion' , 'proveedores_sugeridos', 'numero_contrato', 'numero_requerimiento', 'valor', 'moneda', 'fecha_inicio', 'fecha_terminacion', 'numero_contrato_marco', 'tipo_contrato', 'tipo_contrato_cual', 'numero_pedido_ot_od_os', 'numero_orden_compra', 'nit', 'razon_social', 'numero_consecutivo')



