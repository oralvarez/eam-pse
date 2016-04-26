from django.shortcuts import render
from models import Moneda, Pais, Producto, Localizacion, Cliente, TipoContrato, TipoObjeto, TipoUbicacion
from rest_framework import viewsets
from rest_framework.views import APIView
from transacciones.serializers import  MonedaSerializer, PaisSerializer, ProductoSerializer, LocalizacionSerializer, ClienteSerializer, TipoContratoSerializer, TipoObjetoSerializer, TipoUbicacionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
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
    queryset = Cliente.objects.all().order_by('-nombre')
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
