from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    edad = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()