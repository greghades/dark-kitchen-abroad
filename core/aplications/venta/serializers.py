from rest_framework.serializers import ModelSerializer
from .models import *

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoProductoSerializer(ModelSerializer):
    class Meta:
        model = Pedido_Producto
        fields = '__all__'