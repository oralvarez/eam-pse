from rest_framework import serializers
from models import Moneda, Pais, Departamento, Ciudad, Producto, Localizacion, TipoContrato, TipoUbicacion, TipoObjeto, Cliente, TipoProducto 


class PaisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre',  'codigo_iso')

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre', 'pais')

class CiudadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre', 'departamento')

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

class TipoProductoSerializer(serializers.HyperlinkedModelSerializer):
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
        fields = ('id', 'consecutivo', 'fecha_registro', 'estado', 'usuario', 'fecha_requerido', 'es_secreto', 'objeto', 'localizacion', 'observaciones', 'numero_proceso', 'nivel_inteligencia', 'descripcion_bien_servicio', 'tipo_ubicacion' , 'proveedores_sugeridos', 'numero_contrato', 'numero_requerimiento', 'valor', 'moneda', 'fecha_inicio', 'fecha_terminacion', 'numero_contrato_marco', 'tipo_contrato', 'tipo_contrato_cual', 'numero_pedido_ot_od_os', 'numero_orden_compra', 'nit', 'razon_social', 'numero_consecutivo', 'tipo_producto')
        def validate(self, data):
            """
            Check that the start is before the stop.
            """
            if data['tipo_producto'] == 1:
                if data['tipo_contrato'] == "":
                    raise serializers.ValidationError("No tiene tipo de contrato")
                if data['objeto'] == "":
                    raise serializers.ValidationError("No tiene objeto")
                if data['valor'] <= 0:
                    raise serializers.ValidationError("El valor tiene que ser superior a 0")
                if data['moneda'] == "":
                    raise serializers.ValidationError("Debe seleccionar una moneda")
                if data['numero_contrato'] == "":
                    raise serializers.ValidationError("Debe indicar un numero de contrato")
                if data['observaciones'] == "":
                    raise serializers.ValidationError("Debe tener observaciones")

            return data