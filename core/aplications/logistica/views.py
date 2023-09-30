from rest_framework import viewsets
from .models import Almacen,Ubicación
from .serializers import AlmacenSerializer,UbicaciónSerializer

class AlmacenViewset(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

class UbicaciónViewset(viewsets.ModelViewSet):
    queryset = Ubicación.objects.all()
    serializer_class = UbicaciónSerializer