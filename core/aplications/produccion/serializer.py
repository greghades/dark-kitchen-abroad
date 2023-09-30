from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Produto,Unidad_Medida


class Unidad_MedidaSerializer(ModelSerializer):
    class Meta:
        model = Unidad_Medida
        fields = ('nombre','simbolo')


class ProductSerializer(serializers.ModelSerializer):
    unidad_medida_id = serializers.CharField(source='unidad_medida_id.nombre', read_only=True)
    unidad_medida = serializers.PrimaryKeyRelatedField(
        queryset=Unidad_Medida.objects.all(),
        source='unidad_medida_id',
        write_only=True
    )

    class Meta:
        model = Produto
        fields = ('id', 'nombre', 'descripcion', 'tipo', 'cantidad', 'costo', 'ultimo_cost', 'precio', 'activo', 'fecha_expiracion', 'almacen_id', 'unidad_medida_id', 'unidad_medida', 'proveedor_id')