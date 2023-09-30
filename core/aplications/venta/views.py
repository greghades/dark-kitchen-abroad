from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoProductoViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Producto.objects.all()
    serializer_class = PedidoProductoSerializer
