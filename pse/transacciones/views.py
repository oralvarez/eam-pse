from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from django.views.generic.base import TemplateView

from django.contrib.auth import login, logout
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import QuietBasicAuthentication
from rest_framework import filters
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from django.db.models import Count

from django.db.models import F, Q

# Create your views here.
class PaisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pais.objects.all().order_by('-nombre')
    serializer_class = PaisSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Departamento.objects.all().order_by('-nombre')
    serializer_class = DepartamentoSerializer

class CiudadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Ciudad.objects.all().order_by('-nombre')
    serializer_class = CiudadSerializer

class MonedaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Moneda.objects.all().order_by('-nombre')
    serializer_class = MonedaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cliente.objects.all().order_by('-nit')
    serializer_class = ClienteSerializer

class TipoContratoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoContrato.objects.all().order_by('-nombre')
    serializer_class = TipoContratoSerializer

class TipoObjetoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoObjeto.objects.all().order_by('-nombre')
    serializer_class = TipoObjetoSerializer

class TipoUbicacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoUbicacion.objects.all().order_by('-nombre')
    serializer_class = TipoUbicacionSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TipoProducto.objects.all().order_by('-nombre')
    serializer_class = TipoProductoSerializer

class PaisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pais.objects.all().order_by('-nombre')
    serializer_class = PaisSerializer

class DependenciaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dependencia.objects.all().order_by('-cliente')
    serializer_class = DependenciaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer

#########################
class Anexo_ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anexo_Producto.objects.all().order_by('-id')
    serializer_class = Anexo_ProductoSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(anexo=self.request.data.get('anexo'))

class Estado_ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Estado_Producto.objects.all().order_by('-id')
    serializer_class = Estado_ProductoSerializer

class Detalle_ServicioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Detalle_Servicio.objects.all().order_by('-id')
    serializer_class = Detalle_ServicioSerializer

class Usuario_ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario_Cliente.objects.all().order_by('-id')
    serializer_class = Usuario_ClienteSerializer


class Usuario_ClienteList(generics.ListAPIView):
    serializer_class = Usuario_ClienteSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Usuario_Cliente.objects.all()
        usuario = self.request.query_params.get('usuario', None)
        if usuario is not None:
            queryset = queryset.filter(usuario=usuario)

        cliente = self.request.query_params.get('cliente', None)
        if cliente is not None:
            queryset = queryset.filter(cliente=cliente)

        return queryset

class ProductoListView(generics.ListAPIView):
    """
    Vista para reportes de Productos (Servicios),
    filtrando por parametros.
    """
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def list(self, request):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        tipo_consulta = self.request.query_params.get('tipo_consulta', None)
        tipo_producto = self.request.query_params.get('tipo_producto', None)
        consecutivo = self.request.query_params.get('consecutivo', None)
        estado = self.request.query_params.get('estado', None)
        fecha_registro_desde = self.request.query_params.get('fecha_registro_desde', None)
        fecha_registro_hasta = self.request.query_params.get('fecha_registro_hasta', None)
        nit = self.request.query_params.get('nit', None)
        usuario = self.request.query_params.get('usuario', None)
        asignador = self.request.query_params.get('asignador', None)
        gestor_asignado = self.request.query_params.get('gestor_asignado', None)
        dependencia = self.request.query_params.get('dependencia', None)
        es_secreto = self.request.query_params.get('es_secreto', None)

        queryset = self.get_queryset()

        if tipo_producto is not None:
            if len(tipo_producto) <> 0:
                queryset = queryset.filter(tipo_producto=tipo_producto)

        if consecutivo is not None:
            if len(consecutivo) <> 0:
                queryset = queryset.filter(consecutivo=consecutivo)

        if estado is not None:
            if len(estado) <> 0:
                queryset = queryset.filter(estado=estado)

        if es_secreto is not None:
            if len(es_secreto) <> 0:
                queryset = queryset.filter(es_secreto=es_secreto)

        if dependencia is not None:
            if len(dependencia) <> 0:
                queryset = queryset.filter(id__in=Dependencia.objects.filter(id=dependencia).values('id'))

        if nit is not None:
            if len(nit) <> 0:
                queryset = queryset.filter(id__in=Dependencia.objects.filter(cliente_id__in=Cliente.objects.filter(nit=nit).values('id')).values('id'))

        if usuario is not None:
            if len(usuario) != 0:
                u = User.objects.get(username=usuario)
                queryset = queryset.filter(usuario=u.id)

        if asignador is not None:
            if len(asignador) != 0:
                u = User.objects.get(username=asignador)
                queryset = queryset.filter(asignador=u.id)

        if gestor_asignado is not None:
            if len(gestor_asignado) != 0:
                u = User.objects.get(username=gestor_asignado)
                queryset = queryset.filter(gestor_asignado=u.id)

        if fecha_registro_desde is not None and fecha_registro_hasta is not None:
            if len(fecha_registro_desde) != 0 and len(fecha_registro_hasta) != 0:
                queryset = queryset.filter(fecha_registro__range=[fecha_registro_desde, fecha_registro_hasta])

        if tipo_consulta == "1":
            queryset = queryset.values('tipo_producto__nombre').annotate(conteo=Count('tipo_producto'))

        if tipo_consulta == "2":
            #queryset = queryset.select_related('usuario')
            queryset = queryset.values('usuario__username').annotate(conteo=Count('usuario'))

        if tipo_consulta == "3":
            queryset = queryset.values('estado').annotate(conteo=Count('estado'))

        if tipo_consulta == "4":
            queryset = queryset.values('es_secreto').annotate(conteo=Count('es_secreto'))

        if tipo_consulta == "5":
            queryset = queryset.values('asignador__username').annotate(conteo=Count('asignador'))

        if tipo_consulta == "6":
            queryset = queryset.values('gestor_asignado__username').annotate(conteo=Count('gestor_asignado'))

        if tipo_consulta == "7":
            queryset = queryset.values('nit').annotate(conteo=Count('nit'))

        if tipo_consulta == "8":
            queryset = queryset.values('fecha_registro').annotate(conteo=Count('fecha_registro'))

        queryset = queryset.order_by('-id')

        serializer = ProductoListSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductoConsultaListView(generics.ListAPIView):
    """
    Vista para reportes de Productos (Servicios),
    filtrando por parametros.
    """
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

    def list(self, request):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        tipo_consulta = self.request.query_params.get('tipo_consulta', None)
        tipo_producto = self.request.query_params.get('tipo_producto', None)
        consecutivo = self.request.query_params.get('consecutivo', None)
        estado = self.request.query_params.get('estado', None)
        fecha_registro_desde = self.request.query_params.get('fecha_registro_desde', None)
        fecha_registro_hasta = self.request.query_params.get('fecha_registro_hasta', None)
        nit = self.request.query_params.get('nit', None)
        usuario = self.request.query_params.get('usuario', None)
        asignador = self.request.query_params.get('asignador', None)
        gestor_asignado = self.request.query_params.get('gestor_asignado', None)
        dependencia = self.request.query_params.get('dependencia', None)
        es_secreto = self.request.query_params.get('es_secreto', None)

        queryset = self.get_queryset()

        if tipo_producto is not None:
            if len(tipo_producto) <> 0:
                queryset = queryset.filter(tipo_producto=tipo_producto)

        if consecutivo is not None:
            if len(consecutivo) <> 0:
                queryset = queryset.filter(consecutivo=consecutivo)

        if estado is not None:
            if len(estado) <> 0:
                queryset = queryset.filter(estado=estado)

        if es_secreto is not None:
            if len(es_secreto) <> 0:
                queryset = queryset.filter(es_secreto=es_secreto)

        if dependencia is not None:
            if len(dependencia) <> 0:
                queryset = queryset.filter(id__in=Dependencia.objects.filter(id=dependencia).values('id'))

        if nit is not None:
            if len(nit) <> 0:
                queryset = queryset.filter(id__in=Dependencia.objects.filter(cliente_id__in=Cliente.objects.filter(nit=nit).values('id')).values('id'))

        if usuario is not None:
            if len(usuario) != 0:
                u = User.objects.get(username=usuario)
                queryset = queryset.filter(usuario=u.id)

        if asignador is not None:
            if len(asignador) != 0:
                u = User.objects.get(username=asignador)
                queryset = queryset.filter(asignador=u.id)

        if gestor_asignado is not None:
            if len(gestor_asignado) != 0:
                u = User.objects.get(username=gestor_asignado)
                queryset = queryset.filter(gestor_asignado=u.id)

        if fecha_registro_desde is not None and fecha_registro_hasta is not None:
            if len(fecha_registro_desde) != 0 and len(fecha_registro_hasta) != 0:
                queryset = queryset.filter(fecha_registro__range=[fecha_registro_desde, fecha_registro_hasta])

        if tipo_consulta == "1":
            queryset = queryset.values('tipo_producto__nombre').annotate(conteo=Count('tipo_producto'))

        if tipo_consulta == "2":
            #queryset = queryset.select_related('usuario')
            queryset = queryset.values('usuario__username').annotate(conteo=Count('usuario'))

        if tipo_consulta == "3":
            queryset = queryset.values('estado').annotate(conteo=Count('estado'))

        if tipo_consulta == "4":
            queryset = queryset.values('es_secreto').annotate(conteo=Count('es_secreto'))

        if tipo_consulta == "5":
            queryset = queryset.values('asignador__username').annotate(conteo=Count('asignador'))

        if tipo_consulta == "6":
            queryset = queryset.values('gestor_asignado__username').annotate(conteo=Count('gestor_asignado'))

        if tipo_consulta == "7":
            queryset = queryset.values('nit').annotate(conteo=Count('nit'))

        if tipo_consulta == "8":
            queryset = queryset.values('fecha_registro').annotate(conteo=Count('fecha_registro'))

        serializer = ProductoListSerializer(queryset, many=True)
        return Response(serializer.data)

class DependenciasDetalleServicioList(generics.ListAPIView):
    serializer_class = DependenciaSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Dependencia.objects.filter(cliente_id__in=Cliente.objects.filter(id__in=Usuario_Cliente.objects.filter(usuario=self.request.user).values('cliente_id')))

        return queryset


class Acciones_EstadoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Acciones_Estado.objects.all().order_by('id')
    serializer_class = Acciones_EstadoSerializer


class Acciones_SourcingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Acciones_Sourcing.objects.all().order_by('id')
    serializer_class = Acciones_SourcingSerializer

#########################

#@api_view(['GET'])
def index(request):
    template = loader.get_template('tema3/index_interno.html')
    grupos = request.user.groups.values_list('name', flat=True)
    for g in grupos:
        if g == "Clientes":
            template = loader.get_template('tema3/index_externo.html')
            break

    context = {
        'late': 1,
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))

#@api_view(['GET'])
def reportes_basicos(request):
    template = loader.get_template('tema3/reportes_basicos.html')

    context = {
        'late': 1,
        'user': request.user,
    }
    return HttpResponse(template.render(context, request))

def lista_productos_abastecimiento(request, tipo):
    tp = TipoProducto.objects.get(pk=tipo)
    template = loader.get_template('tema3/lista_productos_abastecimiento.html')
    context = {
        'titulo': tp.nombre,
        'tipo': tipo,
    }
    return HttpResponse(template.render(context, request))

def detalle_producto_abastecimiento(request, id):
    #uc = Usuario_Cliente.objects.filter(usuario=request.user).values('cliente_id')
    #cl = Cliente.objects.filter(id__in=uc)
    #ds = Dependencia.objects.filter(cliente_id__in=cl)
    ds = Dependencia.objects.filter(cliente_id__in=Cliente.objects.filter(id__in=Usuario_Cliente.objects.filter(usuario=request.user).values('cliente_id')))

    template = loader.get_template('tema3/detalle_producto_abastecimiento.html')
    context = {
        'titulo': 'Edicion de Servicio',
        'id' : id,
        'dependencias' : ds
    }
    return HttpResponse(template.render(context, request))

def agregar_producto_abastecimiento(request):
    #for user in User.objects.filter(groups__name='Asignador'):
    #    recipients.append(user.email)

    #for user in User.objects.filter(groups__name='Administradores'):
    #    recipients.append(user.email)

    template = loader.get_template('tema3/detalle_producto_abastecimiento.html')
    context = {
        'titulo': 'Nuevo Servicio',
        'id' : 0,
    }
    return HttpResponse(template.render(context, request))

class AuthView(APIView):
    authentication_classes = (QuietBasicAuthentication,)
 
    def post(self, request, *args, **kwargs):
        login(request, request.user)
        return Response(UserSerializer(request.user).data)
 
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})    

class OnePageAppView(TemplateView):
    template_name = 'transacciones/one_page_app.html'

def login(request):
    template = loader.get_template("tema3/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def logout(request):
    template = loader.get_template("tema3/logout.html")
    context = {}
    return HttpResponse(template.render(context, request))

# class ProductoListView(generics.ListAPIView):
#     serializer_class = ProductoSerializer
#
#     def get_queryset(self):
#         queryset = Producto.objects.all()
#
#         username = self.request.query_params.get('username', None)
#         if username is not None:
#             queryset = queryset.filter(usuario=username)
#         return queryset