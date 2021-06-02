from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings


# Create your models here.
class Carrera(models.Model):
    clave_carrera=models.CharField(max_length=10)
    nombre_carrera=models.CharField(max_length=50)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombre_carrera

class Materia(models.Model):
    clave_materia=models.CharField(max_length=10)
    nombre_materia=models.CharField(max_length=50)
    semestre=models.PositiveSmallIntegerField
    carrera=models.ForeignKey(Carrera, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_materia
