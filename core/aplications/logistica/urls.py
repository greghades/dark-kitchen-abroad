from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router_almacen = DefaultRouter()
router_ubicacion = DefaultRouter()

router_almacen.register(r'almacen',AlmacenViewset)
router_ubicacion.register(r'ubicacion',UbicaciónViewset)

urlpatterns = [
    path('api/', include([
        path('', include(router_almacen.urls)), 
        path('', include(router_ubicacion.urls)),
    ])),
]