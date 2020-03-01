"""URL's de importe del archivo"""

# Django
from django.urls import path

# Views
import file.views as ImporteControl
from file import views

from .filters import RegistroLlamadaFilter

# Filtros
from django_filters.views import FilterView

urlpatterns = [
    path(
        route='importe/',
        view=ImporteControl.upload_excel,
        name='import'
    ),
    path(
        route='entregar/',
        view=views.ListarArchivo.as_view(),
        name='listar_llamada'
    ),
    path(
        route='asignar/',
        view=views.registro_llamada,
        name='asignar'
    ),
    path(
        route='realizar/',
        view=views.registro_llamada,
        name='registrar_llamada'
    ),
    path(
        route='buzon/',
        view=views.ver_Llamadas,
        name='buzon'
    ),
    path(
        route='repartir/',
        view=views.repartir,
        name='repartir'
    ),
    path(
        route='enviar',
        view=views.enviarLlamadas,
        name='enviarLlamada'
    ),
    path(
        route='entregar_l/',
        view=views.entregar.as_view(),
        name='entregar_l'
    ),
    path(
        route='entrega',
        view=views.ver_Llamadas,
        name='entrega'
    ),
    path(
        route='eliminar',
        view=views.archivoLlamadas.as_view(),
        name='eliminar'
    ),
    path(
        route='borrar',
        view=views.eliminarArchivo,
        name='delete'
    ),
    path(
        route='traer',
        view=views.traer,
        name='traer'
    ),
    path(
        route='verllamadas',
        view=views.ver_Llamadas,
        name='borrar'
    ),
    path(
        route='prueballamadas',
        view=views.pruebas_llamadas,
        name='prueballamada'
    ),
    path(
        route='prueba/<int:number>/',
        view=views.realizar_llamada,
        name='prueba'
    ),
]
