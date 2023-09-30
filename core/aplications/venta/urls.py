from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router_cliente = DefaultRouter()
router_pedido = DefaultRouter()
router_PedidoProducto = DefaultRouter()

router_cliente.register(r'cliente',ClienteViewSet)
router_pedido.register(r'pedido',PedidoViewSet)
router_PedidoProducto.register(r'pedidoProducto',PedidoProductoViewSet)

urlpatterns = [
    path('api/', include([
        path('', include(router_cliente.urls)), 
        path('', include(router_pedido.urls)),
        path('', include(router_PedidoProducto.urls)),  
    ])),
]
