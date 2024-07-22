from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('autor_list/', views.autorlist, name='autores'),
    path('cliente_list/', views.cliente, name='cliente'),
    path('proveedor_list/', views.proveedor, name='proveedor'),
    path('producto_list/', views.producto, name='producto'),
    path('crud/', views.crud, name='crud'),
    path('crud/agregar', views.agregar, name='agregar'),
    path('cliente_list/<int:id>/editar', views.editar, name='edit1'),
    path('cliente_list/<int:id>/edit', views.editar, name='edit'),
    path('cliente_list/<int:id>/eliminar', views.borrar, name='bor'),
]+static (settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)