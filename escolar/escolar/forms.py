from django import forms
from .models import Carrera, Materia

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['clave_carrera']

class MateriaForm(forms.ModelForm):
    def __init__(self, idcreador,*args, **kwargs):
        super(MateriaForm, self).__init__(*args, **kwargs)
        self.fields['carrera'].queryset=Carrera.objects.filter(creador=idcreador)
    class Meta:
        model = Materia
        fields = ['clave_materia', 'carrera']

    def clean(self):
        super(MateriaForm, self). clean()
        clave_opc = self,cleaned_data.get('clave_materia')
        if not clave_materia.startswith("A"):
            self.add_error('clave_materia','No esta comenzando con A')
        return self.cleaned_data