from django.db import models

class Autor(models.Model):
    id= models.SmallIntegerField(verbose_name='id',primary_key=True)
    nombre = models.CharField(verbose_name='nombre', max_length=100,default='')
    last_name = models.CharField(verbose_name='apellido', max_length=100,default='')
    age = models.PositiveSmallIntegerField(verbose_name='edad')
    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id= models.SmallIntegerField(verbose_name='id',primary_key=True)
    nombre = models.CharField(verbose_name='nombre',max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Proveedor(models.Model):
    id= models.SmallIntegerField(verbose_name='id',primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id= models.SmallIntegerField(verbose_name='id',primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedores = models.ManyToManyField(Proveedor)
    def __str__(self):
        return self.nombre  