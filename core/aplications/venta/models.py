from django.db import models
from aplications.authentication.models import CustomUser
from aplications.produccion.models import Produto
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    cedula = models.CharField(max_length=50, null=False)
    telefono = models.CharField(max_length=50,null=False)
    email = models.EmailField(max_length=200, unique=True)
    activo = models.BooleanField(default=False)
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)

class Pedido(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total =  models.FloatField()
    fecha = models.DateField(auto_now_add=True)
    pagado = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)

class Pedido_Producto(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    