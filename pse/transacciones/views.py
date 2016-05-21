from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from django.views.generic.base import TemplateView

from django.contrib.auth import login, logout
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import QuietBasicAuthentication
from rest_framework import filters
from rest_framework import generics

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

class LocalizacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Localizacion.objects.all().order_by('-cliente')
    serializer_class = LocalizacionSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all().order_by('-consecutivo')
    serializer_class = ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Producto.objects.all().order_by('-consecutivo')
    serializer_class = ProductoSerializer

#########################
class Anexo_ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Anexo_Producto.objects.all().order_by('-id')
    serializer_class = Anexo_ProductoSerializer

class Estado_ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Estado_Producto.objects.all().order_by('-id')
    serializer_class = Estado_ProductoSerializer

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
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(usuario=username)
        return queryset

# class Usuario_ClienteView(generics.ListAPIView):
#     queryset = Usuario_Cliente.objects.all()
#     serializer = Usuario_ClienteSerializer
#     filter_backends = (filters.DjangoFilterBackend,)

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

@api_view(['GET'])
def index(request):

    template = loader.get_template('tema3/index.html')
    context = {
        'late': 1,
        'user' : request.user,
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
    template = loader.get_template('tema3/detalle_producto_abastecimiento.html')
    context = {
        'titulo': 'Edicion de Servicio',
        'id' : id,
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