from rest_framework.serializers import ModelSerializer
from .models import Produto


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'