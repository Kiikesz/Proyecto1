from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)


class Profesor(models.Model):
    
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.EmailField(max_length=40)
    profesion = models.CharField(max_length=20)
    edad = models.IntegerField(default=0)


class Entregable(models.Model):
        nombre = models.CharField(max_length=20)
        fecha = models.DateField()
        entregado = models.BooleanField()

class  Curso(models.Model):
     nombre = models.CharField(max_length=20)
     camada = models.IntegerField()
     comision = models.IntegerField()


class Familiar (models.Model):
    parentesco = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha = models.DateField()
