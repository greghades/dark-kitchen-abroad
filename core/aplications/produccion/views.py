from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    RetrieveDestroyAPIView
)
from .serializer import ProductSerializer
from .models import Produto



# Create your views here.

class List_product(ListAPIView):
    serializer_class = ProductSerializer
    queryset = Produto.objects.all()

class Detail_product(RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Produto.objects.filter()

class Create_product(CreateAPIView):
    serializer_class = ProductSerializer

class Update_product(RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Produto.objects.all()

class Delete_product(RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Produto.objects.all()