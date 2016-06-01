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
router.register(r'dependencia', DependenciaViewSet)
router.register(r'tipocontrato', TipoContratoViewSet)
router.register(r'tipoobjeto', TipoObjetoViewSet)
router.register(r'tipoubicacion', TipoUbicacionViewSet)
router.register(r'tipoproducto', TipoProductoViewSet)

router.register(r'anexoproducto', Anexo_ProductoViewSet)
router.register(r'estadoproducto', Estado_ProductoViewSet)
router.register(r'usuariocliente', Usuario_ClienteViewSet)
router.register(r'accionesestado', Acciones_EstadoViewSet)
router.register(r'accionessourcing', Acciones_SourcingViewSet)
router.register(r'detallesolicitudproducto', Detalle_ServicioViewSet)
#router.register(r'productolist', ProductoListView)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    #url(r'^api/productolist/', ProductoListView),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^dashboard/$', index, name="index"),
    url(r'^logout/$', logout, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login, name="login"),
    url(r'^nav/abastecimiento/servicios/$', index, name="index_servicios"),
    url(r'^nav/abastecimiento/servicios/detalle/(?P<id>\d+)$', detalle_producto_abastecimiento, name='detalle_producto_abastecimiento'),
    url(r'^nav/abastecimiento/servicios/nuevo/$', agregar_producto_abastecimiento, name='agregar_producto_abastecimiento'),
    #url(r'^filtros/dependencias/$', Usuario_ClienteList.as_view()),
    url(r'^filtros/dependencias/$', DependenciasDetalleServicioList.as_view()),
    url(r'^filtros/productos/$', ProductoListView.as_view()),
    url(r'^filtros/consultas/$', ProductoConsultaListView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
