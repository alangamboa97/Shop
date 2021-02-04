from rest_framework import serializers
from .models import Categoria_Mat, Categoria_Prod, Producto, Material, Producto_Material, Temporada

class CategoriaMSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_Mat
        fields = ('idCategoriaCatM', 'nombreCatM', 'descripcionCatM')

class CategoriaPSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_Prod
        fields = ('idCategoriaCatP', 'nombreCatP', 'descripcionCatP')

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ('idMaterial', 'idCategoriaMat', 'descripcionMat', 'nombreMat', 'costoMat', 'cantidadMat', 'unidadMat', 'created_at')

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = ('id', 'descripcionTemp', 'nombreTemp', 'fechaInicio', 'fechaFin')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('idProducto', 'idCategoriaProd', 'descripcionProd', 'nombreProd', 'imgProd', 'precioProd', 'temporada', 'created_at')

class Producto_MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto_Material
        fields = ('id', 'idMaterial', 'idProducto', 'cantidad', 'tipo')