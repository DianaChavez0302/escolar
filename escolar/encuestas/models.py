from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings


# Create your models here.
class Pregunta(models.Model):
    texto_pregunta=models.CharField(max_length=210)
    fecha_pub=models.DateTimeField('fecha de publicacion', auto_now_add=True)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_pregunta

    def es_reciente(self):
        return self.fecha_pub >=timezone.now() - datetime.timedelta(days=1) ##fecha en teimpo real menos un dia

    es_reciente.admin_order_field = 'fecha_pub'
    es_reciente.short_description = 'Publicada recientemente?'
    es_reciente.boolean = True

class Opcion(models.Model):
    texto_opcion=models.CharField(max_length=200)
    num_votos=models.IntegerField(default=0)
    pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_opcion
