from rest_framework.serializers import ModelSerializer
from .models import *


class AlmacenSerializer(ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'
class UbicaciónSerializer(ModelSerializer):
     class Meta:
        model = Ubicación
        fields = '__all__'