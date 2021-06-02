from django.db import models

# Create your models here.
class Pregunta(models.Model):
    texto_pregunta=models.CharField(max_length=210)
    fecha_pub=models.DateTimeField()

    def __str__(self):
        return self.texto_pregunta

class Opcion(models.Model):
    texto_opcion=models.CharField(max_length=200)
    num_votos=models.IntegerField(default=0)
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_opcion
