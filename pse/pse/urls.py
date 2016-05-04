"""pse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from quickstart import views
from transacciones.views import *
from .admin import admin_site
from . import settings
 
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'moneda', MonedaViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'departamento', DepartamentoViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'producto', ProductoViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'localizacion', LocalizacionViewSet)
router.register(r'tipocontrato', TipoContratoViewSet)
router.register(r'tipoobjeto', TipoObjetoViewSet)
router.register(r'tipoubicacion', TipoUbicacionViewSet)
router.register(r'tipoproducto', TipoProductoViewSet)


urlpatterns = [
    url(r'^api/', include(router.urls)),
    #url(r'^', OnePageAppView.as_view(), name='home'),
    #url(r'^api/auth/$', transacciones.views.AuthView.as_view(), name='authenticate')
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/auth/$', AuthView.as_view(), name='authenticate'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^nav/abastecimiento/productos/(?P<tipo>[0-9])/$', productos, name='productos'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
