from django.http import HttpResponse
from django.template import loader
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from django.views.generic.base import TemplateView

from django.contrib.auth import login, logout
from django.shortcuts import render
from models import Moneda, Pais, Producto, Localizacion, Cliente, TipoContrato, TipoObjeto, TipoUbicacion, TipoProducto, Departamento, Ciudad
from rest_framework import viewsets
from rest_framework.views import APIView
from transacciones.serializers import  MonedaSerializer, DepartamentoSerializer, CiudadSerializer, PaisSerializer, ProductoSerializer, LocalizacionSerializer, ClienteSerializer, TipoContratoSerializer, TipoObjetoSerializer, TipoUbicacionSerializer, TipoProductoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import QuietBasicAuthentication

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


@api_view(['GET'])
def poe(request):
    template = loader.get_template('transacciones/index.html')
    context = {
        'late': 1,
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