from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Invernadero(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre Invernadero')
    ubicacion = models.CharField(max_length=255, verbose_name='Ubicacion')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Sensor(models.Model):
    TIPO_SENSOR =(
        ('T','Temperatura'),
        ('H','Humedad'),
        ('L','Luz'),
        ('M','Movimiento'),
    )
    nombre = models.CharField(max_length=100, verbose_name='Nombre Sensor')
    tipo = models.CharField(max_length=1, choices=TIPO_SENSOR , verbose_name='Tipo snesor')
    invernadero = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name}({self.get_tipo_display})'
    