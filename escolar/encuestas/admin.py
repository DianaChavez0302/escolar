from django.contrib import admin
from .models import Pregunta, Opcion

# Register your models here.
class OpcionEnPregunta(admin.TabularInline):
    model = Opcion
    extra=3
#admin.site.register(Opcion)
class PreguntaAdmin(admin.ModelAdmin):
 #   fields = ['fecha_pub', 'texto_pregunta']
    fieldsets = [
        ('Información de fecha', {'fields':['fecha_pub']} ),
        (None, {'fields':['texto_pregunta']})
    ]
    inlines = [ OpcionEnPregunta ]
    list_display = ('texto_pregunta', 'fecha_pub', 'es_reciente')
    list_filter = [ 'fecha_pub' ]
    search_fields = [ 'texto_pregunta' ]
admin.site.register(Pregunta, PreguntaAdmin)