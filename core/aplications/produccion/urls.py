from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router_producto = DefaultRouter()

router_producto.register(r'producto',ProductViewset)

urlpatterns = [
    
    path('api/', include([
        path('',include(router_producto.urls)),
    ])),
]
