from django.db import models
from usuario.models import Perfil
from utils.models import BaseModel

class Grabacion(BaseModel, models.Model):
    # Url de donde va quedar almacenada la grabacion
    url = models.URLField()


class Estado(BaseModel, models.Model):
    nombre = models.CharField(max_length=30)


class RegistroLlamada(BaseModel, models.Model):
    nombre_contesta = models.CharField(max_length=45)
    fecha_entrega = models.DateField()
    observaciones = models.TextField(null=True, blank=True)
    precio_llamada = models.FloatField()
    numero_contesta = models.CharField(max_length=20)
    id_usuario = models.ForeignKey(Perfil, on_delete=models.PROTECT)
    id_estado = models.ForeignKey('Estado', on_delete=models.PROTECT)
    id_grabacion = models.ForeignKey('Grabacion', on_delete=models.PROTECT)
