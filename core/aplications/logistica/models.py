from django.db import models
from aplications.produccion.models import Produto

# Create your models here.
class Almacen(models.Model):
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)
    nombre = models.CharField(max_length=50, null=False)
    tipo = 0
    maximo = models.IntegerField()
    minimo = models.IntegerField()
    activo = models.BooleanField(default=False)

class Ubicación(models.Model):
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)
    nombre = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    fila = models.IntegerField()
    columna = models.IntegerField()
    pasillo = models.IntegerField()
    cantidad_limite = models.IntegerField()
    cantidad = models.IntegerField()
    almacen_id = models.ForeignKey(Almacen,on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)

