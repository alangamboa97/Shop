from django.shortcuts import render
from rest_framework import generics
from .serializers import CategoriaMSerializer, CategoriaPSerializer, ProductoSerializer, MaterialSerializer, TemporadaSerializer, Producto_MaterialSerializer
from .models import Categoria_Mat, Categoria_Prod, Producto, Material, Producto_Material, Temporada

# Create your views here.
class CategoriaMView(generics.CreateAPIView):
    queryset = Categoria_Mat.objects.all()
    serializer_class = CategoriaMSerializer

class CategoriaPView(generics.CreateAPIView):
    queryset = Categoria_Prod.objects.all()
    serializer_class = CategoriaPSerializer

class TemporadaView(generics.CreateAPIView):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer

class ProductoView(generics.CreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class MaterialView(generics.CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class Producto_MaterialView(generics.CreateAPIView):
    queryset = Producto_Material.objects.all()
    serializer_class = Producto_MaterialSerializer