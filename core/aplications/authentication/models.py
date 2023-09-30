from django.db import models
from django.contrib.auth.models import AbstractUser,Permission

# Create your models here.
USER_ROLES_CHOICES = (
    ('Usuario', 'usuario'),
    ('Producción', 'produccion'),
    ('Ventas', 'ventas'),
    ('Logistica', 'logistica'),
)

class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)   
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=150,null=False)
    rol = models.CharField(max_length=50,choices=USER_ROLES_CHOICES)
    codigo = models.CharField(max_length=50)
    activo = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return f"{self.get_full_name()}"
    
class CodesVerification(models.Model):
    changePasswordCode = models.CharField(max_length=10,unique=True)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL) 
    def __str__(self):
        return f"{self.user}"

class Permisos(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=50,blank=False,null=False,unique=True)
    activo = models.BooleanField(default=False)

class Permiso_usuario(models.Model):
    id_usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id_peromiso = models.ForeignKey(Permisos, on_delete=models.CASCADE)