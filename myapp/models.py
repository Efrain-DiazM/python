from email.policy import default
from random import choices
from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(AbstractUser):
    rol = models.CharField(max_length=30)

class Programa(models.Model):
    codigo = models.CharField(max_length=5, primary_key=True)
    nombrePrograma = models.CharField(max_length=30)
    duracion = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        text = "{0} (Duracion: {1} Año(s))"
        return text.format(self.nombrePrograma, self.duracion)
    
class UserCourse(models.Model):
    identificacion = models.CharField(max_length=10, primary_key=True)
    roles = [
        ('Admin', 'Admin'),
        ('Profesor', 'Profesor'),
        ('Alumno', 'Alumno')
    ]
    rol = models.CharField(max_length=9, choices=roles, default='Alumno')
    apellidos = models.CharField(max_length=30)
    nombres = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    generos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    genero = models.CharField(max_length=1, choices=generos, default='F')
    programa = models.ForeignKey(Programa, null=False, blank=False, on_delete=models.CASCADE)
    validacion = models.BooleanField(default=True) 

    def nombreCompleto(self):
        text = "{0}, {1}"
        return text.format(self.apellidos, self.nombres)
    
    def __str__(self):
        text = "{0} / Programa: {1} / {2}"
        if self.validacion:
            estado = "Activo"
        else:
            estado = "Inactivo"
        return text.format(self.nombreCompleto(), self.programa, estado)

class crearCurso(models.Model):
    idCurso = models.CharField(max_length=10, primary_key=True)
    nombreCurso = models.CharField(max_length=30)
    numeroCreditos = models.CharField(max_length=3)
    tipoPrograma = models.CharField(max_length=10)
    programaPertenece = models.CharField(max_length=30)
    semestre = models.CharField(max_length=2)
    descripcion = models.CharField(max_length=200)
    profesorCurso = models.ForeignKey(UserCourse, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        text = "{0}"
        return text.format(self.nombreCurso)
    
class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    alumno = models.ForeignKey(UserCourse, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(crearCurso, null=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
