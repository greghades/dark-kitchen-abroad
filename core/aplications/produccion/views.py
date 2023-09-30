from django.shortcuts import render
from rest_framework import viewsets
from .models import Produto
from .serializer import ProductSerializer
# Create your views here.

class ProductViewset(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProductSerializer


