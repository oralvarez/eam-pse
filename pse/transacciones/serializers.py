from rest_framework import serializers
from models import Moneda, Pais, Departamento, Ciudad, Producto, Dependencia, TipoContrato, TipoUbicacion, TipoObjeto, Cliente, TipoProducto, Anexo_Producto, Estado_Producto, Usuario_Cliente, Acciones_Estado, Acciones_Sourcing, Detalle_Servicio


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre',  'codigo_iso')

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ('id', 'nombre', 'pais')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre', 'departamento')

class MonedaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moneda
        fields = ('id', 'nombre', 'descripcion', 'pais')

class TipoContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContrato
        fields = ('id', 'nombre', 'descripcion')

class TipoUbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUbicacion
        fields = ('id', 'nombre', 'descripcion')

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ('id', 'nombre', 'descripcion')

class TipoObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoObjeto
        fields = ('id', 'nombre', 'descripcion')

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ('id', 'nombre', 'codigo_iso')

class ClienteSerializer(serializers.ModelSerializer):
    logo = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Cliente
        fields = ('id', 'nit', 'razon_social', 'direccion', 'ciudad', 'telefono', 'datos_contacto', 'logo')

class DependenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependencia
        fields = ('id', 'cliente', 'identificacion', 'nombre', 'codigo', 'tipo', 'dependencia_padre')

class Acciones_SourcingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acciones_Sourcing
        fields = ('id', 'descripcion')

class Acciones_EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acciones_Estado
        fields = ('id', 'descripcion')

class Usuario_ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario_Cliente
        fields = ('id', 'cliente', 'usuario', 'vigencia_fecha_desde', 'vigencia_fecha_hasta')

class Anexo_ProductoSerializer(serializers.ModelSerializer):
    anexo = serializers.FileField(max_length=None, use_url=True)

    class Meta:
        model = Anexo_Producto
        fields = ('id', 'producto', 'usuario', 'anexo', 'fecha', 'descripcion')

class Estado_ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Producto
        fields = ('id', 'producto', 'usuario', 'estado_anterior', 'accion', 'estado_actual', 'fecha', 'descripcion')

class Detalle_ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detalle_Servicio
        fields = ('id', 'producto', 'dependencia', 'porcentaje', 'funcionario_autorizado')

class ProductoListSerializer(serializers.Serializer):
    #item = serializers.CharField()
    id = serializers.IntegerField(required=False)
    consecutivo = serializers.CharField(required=False)
    tipo_producto = serializers.CharField(required=False)
    tipo_producto__nombre = serializers.CharField(required=False)
    estado = serializers.CharField(required=False)
    usuario__username = serializers.CharField(required=False)
    es_secreto = serializers.CharField(required=False)
    asignador__username = serializers.CharField(required=False)
    gestor_asignado__username = serializers.CharField(required=False)
    nit = serializers.CharField(required=False)
    fecha_registro = serializers.DateField(required=False)
    observaciones = serializers.CharField(required=False)
    conteo = serializers.IntegerField(required=False)

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id', 'consecutivo', 'fecha_registro', 'estado', 'usuario', 'fecha_requerido', 'es_secreto', 'objeto', 'observaciones', 'numero_proceso', 'nivel_inteligencia', 'descripcion_bien_servicio', 'tipo_ubicacion' , 'proveedores_sugeridos', 'numero_contrato', 'numero_requerimiento', 'valor', 'moneda', 'fecha_inicio', 'fecha_terminacion', 'numero_contrato_marco', 'tipo_contrato', 'tipo_contrato_cual', 'numero_pedido_ot_od_os', 'numero_orden_compra', 'nit', 'razon_social', 'numero_consecutivo', 'tipo_producto', 'gestor_asignado', 'asignador')

            # def validate(self, data):
    #     """
    #     Check that the start is before the stop.
    #     """
    #     # if data['tipo_producto'] == 1:
    #     #     if data['tipo_contrato'] == "":
    #     #         raise serializers.ValidationError("No tiene tipo de contrato")
    #     #     if data['objeto'] == "":
    #     #         raise serializers.ValidationError("No tiene objeto")
    #     #     if data['valor'] <= 0:
    #     #         raise serializers.ValidationError("El valor tiene que ser superior a 0")
    #     #     if data['moneda'] == "":
    #     #         raise serializers.ValidationError("Debe seleccionar una moneda")
    #     #     if data['numero_contrato'] == "":
    #     #         raise serializers.ValidationError("Debe indicar un numero de contrato")
    #     #
    #     # if data['observaciones'] == "":
    #     #     raise serializers.ValidationError("Debe tener observaciones")
    #
    #     return data