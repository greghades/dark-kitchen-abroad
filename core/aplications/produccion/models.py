from django.db import models

produccionS_CHOICES = (
    ('ingrediente', 'Ingrediente'),
    ('platillo ', 'platillo '),
    ('insumo', 'insumo'),
)

ESTADOS_CALIDAD_CHOICES = (
    ('fresco', 'Fresco'),
    ('maduro', 'Maduro'),
    ('en_su_punto', 'En su punto'),
    ('pasado', 'Pasado'),
    ('podrido', 'Podrido'),
)

USOS_produccionS_CHOICES = (
    ('verduras_ensalada', 'Ensalada de verduras frescas'),
    ('verduras_salteado', 'Salteado de verduras'),
    ('verduras_sopa', 'Sopa de verduras'),
    ('carnes_parrillada', 'Parrillada de carne'),
    ('carnes_estofado', 'Estofado de carne'),
    ('carnes_hamburguesa', 'Hamburguesa de carne'),
    ('pescado_sushi', 'Sushi de pescado fresco'),
    ('pescado_ceviche', 'Ceviche de pescado y mariscos'),
    ('pescado_filete', 'Filete de pescado a la parrilla'),
    ('frutas_batidos', 'Batidos de frutas frescas'),
    ('frutas_tarta', 'Tarta de frutas'),
    ('frutas_mermelada', 'Mermelada de frutas'),
    ('lacteos_macarrones', 'Macarrones con queso'),
    ('lacteos_helado', 'Helado de leche y crema'),
    ('lacteos_mantequilla', 'Mantequilla para cocinar y hornear'),
)

class Unidad_Medida(models.Model):
    nombre = models.CharField(max_length=25,blank=False,null=False)
    simbolo = models.CharField(max_length=3,blank=False,null=False)
    activo = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=25,blank=False,null=False)
    rif = models.CharField(max_length=10,blank=False,null=False)
    telefono = models.CharField(max_length=11,blank=False,null=False)
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)
    activo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=25,blank=False,null=False)
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)
    activo = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre

# Create your models here.
class Produto(models.Model):
    nombre = models.CharField(max_length=25,blank=False,null=False)
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)
    unidad_medida_id = models.ForeignKey(Unidad_Medida, on_delete=models.CASCADE)
    costo = models.FloatField(blank=False,null=False)
    ultimo_cost = models.FloatField(blank=False,null=False)
    activo = models.BooleanField(default=False)
    precio = models.FloatField(blank=False,null=False)
    descripcion = models.TextField(max_length=50,blank=False,null=False,unique=True)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50,blank=False,null=False,choices=produccionS_CHOICES)
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_expiracion = models.DateField()
    estado = models.CharField(max_length=50,blank=False,null=False,choices=ESTADOS_CALIDAD_CHOICES)
    uso = models.CharField(max_length=50,blank=False,null=False,choices=USOS_produccionS_CHOICES)

    def __str__(self):
        return self.nombre + self.tipo
class Menu(models.Model):
    nombre = models.CharField(max_length=25,blank=False,null=False)
    codigo = models.CharField(max_length=50,blank=False,null=False,unique=True)
    activo = models.BooleanField(default=False)
    def __str__(self):
        return self.nombre
class Menu_Producto(models.Model):
    menu_id = models.ForeignKey(Menu,on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)

class Ingrediente(models.Model):
    platillo_id = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name="platillo")
    ingrediente_id = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name="ingrediente")
    cantidad = models.IntegerField()