from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Produto,Unidad_Medida


class Unidad_MedidaSerializer(ModelSerializer):
    class Meta:
        model = Unidad_Medida
        fields = ('nombre','simbolo')


class ProductSerializer(ModelSerializer):
    unidad_medida_id = Unidad_MedidaSerializer()  # Utiliza el serializer de Unidad_Medida

    class Meta:
        model = Produto
        fields = ('id', 'nombre', 'descripcion', 'tipo', 'cantidad', 'costo', 'ultimo_cost', 'precio', 'activo', 'fecha_expiracion', 'almacen_id', 'unidad_medida_id', 'proveedor_id')