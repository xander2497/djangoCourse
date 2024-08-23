from django.db import models

# Create your models here.

class departamento(models.Model):
    nombreDepartamento = models.CharField(max_length=48, null=True, blank=True)
    descripcionDepartamento = models.CharField(max_length=256, null=True, blank=True)


class persona(models.Model):
    nombre = models.CharField(max_length=32, null=True, blank=True)
    apellido = models.CharField(max_length=32, null=True, blank=True)
    numero = models.CharField(max_length=24, null=True, blank=True)
    email = models.CharField(max_length=48, null=True, blank=True)
    descripcion = models.CharField(max_length=256, null=True, blank=True)
    depaRelacionado = models.ForeignKey(departamento, null=True, blank=True, on_delete=models.SET_NULL)