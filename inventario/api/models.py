from django.db import models

# Create your models here.
class Categoria_Mat(models.Model):
    idCategoriaCatM = models.AutoField(primary_key=True)
    nombreCatM = models.CharField(max_length=50)
    descripcionCatM = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class Categoria_Prod(models.Model):
    idCategoriaCatP = models.AutoField(primary_key=True)
    nombreCatP = models.CharField(max_length=50)
    descripcionCatP = models.CharField(max_length=50)

    def __str__(self):
        return super().__str__()

class Material(models.Model):
    idMaterial = models.AutoField(primary_key=True)
    idCategoriaMat = models.ForeignKey(Categoria_Mat, on_delete=models.CASCADE)
    descripcionMat = models.CharField(max_length=100)
    nombreMat = models.CharField(max_length=50)
    costoMat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    cantidadMat = models.IntegerField(default=0)
    unidadMat = models.CharField(max_length=10, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()

class Temporada(models.Model):
    descripcionTemp = models.CharField(max_length=100)
    nombreTemp = models.CharField(max_length=50)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    idCategoriaProd = models.ForeignKey(Categoria_Prod, on_delete=models.CASCADE)
    descripcionProd = models.CharField(max_length=100)
    nombreProd = models.CharField(max_length=50)
    imgProd = models.ImageField(upload_to ='media/productos', null=True, blank=True) 
    precioProd = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return super().__str__()

class Producto_Material(models.Model):
    CATEGORY = (
        ('0', 'necesario'),
        ('1', 'extra'),
    )
    idMaterial = models.ForeignKey(Material, on_delete=models.CASCADE)
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=1, choices = CATEGORY)


