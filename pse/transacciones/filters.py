import rest_framework.filters as filters
from .models import *

class LocalizacionFilter(filters.FilterSet):
    usuario = filters.CharFilter(name="usuario__name")

    class Meta:
        model = Localizacion
        fields = ['cliente', 'identificacion', 'nombre', 'codigo', 'tipo']
