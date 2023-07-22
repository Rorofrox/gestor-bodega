from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class PerfilUsuario(AbstractUser):
    JEFEBODEGA = 'JF'
    BODEGUERO = 'BD'
    ROLES_USUARIO = [
        (JEFEBODEGA, 'Jefe de Bodega'),
        (BODEGUERO, 'Bodeguero'),
    ]
    rol = models.CharField(max_length=2, choices=ROLES_USUARIO, default=BODEGUERO)

    def es_jefe_bodega(self):
        return self.rol == self.JEFEBODEGA

    def es_bodeguero(self):
        return self.rol == self.BODEGUERO
    
    groups = models.ManyToManyField(Group, related_name='perfil_usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='perfil_usuarios')

class Bodega(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100, default='Valor predeterminado')
    jefe_bodega = models.ForeignKey(PerfilUsuario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre

    def stock_producto(self, producto):
        return self.productos.filter(id=producto.id).count()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    bodegas = models.ManyToManyField(Bodega, related_name='productos')
    cantidad_producto = models.IntegerField(default=0)  # Agregamos el campo cantidad_producto como un entero con valor inicial 0

    def __str__(self):
        return self.nombre


class Movimiento(models.Model):
    bodega_origen = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='movimientos_salida')
    bodega_destino = models.ForeignKey(Bodega, on_delete=models.CASCADE, related_name='movimientos_entrada')
    productos = models.ManyToManyField(Producto, through='DetalleMovimiento')
    usuario = models.ForeignKey(PerfilUsuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)

class DetalleMovimiento(models.Model):
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE, blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
