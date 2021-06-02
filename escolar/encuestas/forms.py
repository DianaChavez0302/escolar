from django import forms
from .models import Pregunta, Opcion

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['texto_pregunta']

class OpcionForm(forms.ModelForm):
    def __init__(self, idcreador,*args, **kwargs):
        super(OpcionForm, self).__init__(*args, **kwargs)
        self.fields['pregunta'].queryset=Pregunta.objects.filter(creador=idcreador)
    class Meta:
        model = Opcion
        fields = ['texto_opcion', 'pregunta']

    def clean(self):
        super(OpcionForm, self). clean()
        texto_opc = self,cleaned_data.get('texto_opcion')
        if not texto_opcion.startswith("A"):
            self.add_error('texto_opcion','No esta comenzando con A')
        return self.cleaned_data