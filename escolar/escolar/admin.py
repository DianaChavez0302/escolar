from django.contrib import admin
from .models import Carrera, Materia

# Register your models here.
class MateriaEnCarrera(admin.TabularInline):
    model = Materia
    extra=3
#admin.site.register(Opcion)
class CarreraAdmin(admin.ModelAdmin):
    search_fields = [ 'clave_carrera' ]
admin.site.register(Carrera, CarreraAdmin)