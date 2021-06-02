from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Pregunta, Opcion
from django.urls import reverse, reverse_lazy #funciones, clases
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PreguntaForm, OpcionForm
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
class IndexView(generic.ListView):
    # Por default la plantilla seria pregunta_list.html
    template_name="encuestas/index.html"
    # Por default la variable con la lista de objetos se llamaria pregunta_list
    context_object_name="lista_preguntas_recientes"

    def get_queryset(self):
        return Pregunta.objects.order_by('-fecha_pub')[:10]


class DetalleView(LoginRequiredMixin, generic.DetailView):
    # Por default la pantilla se llamaria pregunta.detail.html
    # Por default la variable en la plantilla se llamaria pregunta
    template_name="encuestas/detalle.html"
    model=Pregunta

#Esta vista permite votar para una pregunta
#URL: http://xxxx.pythonanywhere.com/encuestas/<id>/votar

@login_required
def votar(request, id_pregunta):
    p=get_object_or_404(Pregunta, pk=id_pregunta)
    try:
         opcion_sel = p.opcion_set.get(pk=request.POST['opcion'])
    except(Opcion.DoesNotExist, KeyError ):
        contexto ={
            'pregunta' : p,
            'mensaje_error': 'Debes seleccionar una opcion valida'
        }
        return render(request, 'encuestas/detalle.html', contexto)
    else:
        opcion_sel.num_votos += 1
        opcion_sel.save()
        #solicitar al cliente que cargue otra pagina(redireccion)
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(p.id,)))

class ResultadosView( generic.DetailView):
    # Por default la pantilla se llamaria pregunta.detail.html
    # Por default la variable en la plantilla se llamaria pregunta
    template_name="encuestas/resultados.html"
    model=Pregunta

class PreguntaCreaView(LoginRequiredMixin, View):
    template_name="encuestas/pregunta_form.html"
    success_url=reverse_lazy("encuestas:index")
    def get(self, request):
        forma = PreguntaForm()
        contexto={
            'form': forma #diccionario de formas
        }
        return render(request,self.template_name, contexto)

    def post(self, request):
        forma = PreguntaForm(request.POST)
        if not forma.is_valid():
            contexto = {
                'form': forma
            }
            return render(request,self.template_name, contexto)
        pregunta = forma.save(commit=False)
        pregunta.creador = self.request.user
        pregunta.save()
        return redirect(self.success_url)

class PreguntaEditaView(LoginRequiredMixin, UpdateView):
    model= Pregunta
    success_url = reverse_lazy("encuestas:index")
    fields = ('texto_pregunta',)


class PreguntaEliminaView(LoginRequiredMixin, DeleteView):
    model= Pregunta
    success_url = reverse_lazy("encuestas:index")

  #  fields = ('texto_pregunta',)

class OpcionIndexView(generic.ListView):
    model = Opcion
    paginate_by = 5

class OpcionCreaView(LoginRequiredMixin, View):
    template_name="encuestas/opcion_form.html"
    success_url=reverse_lazy("encuestas:index_opcion")
    def get(self, request):
        forma = OpcionForm(self.request.user)
        contexto={
            'form': forma #diccionario de formas
        }
        return render(request,self.template_name, contexto)

    def post(self, request):
        forma = OpcionForm(self.request.user, request.POST)
        if not forma.is_valid():
            contexto = {
                'form': forma
            }
            return render(request,self.template_name, contexto)

        return redirect(self.success_url)

class OpcionEditaView(LoginRequiredMixin, View):
    template_name="encuestas/opcion_form.html"
    success_url=reverse_lazy("encuestas:index_opcion")
    def get(self, request, pk):
        opcion = get_object_or_404(Opcion, pk=pk) #primer pk llave primaria, segundo pk lo que recibo
        forma = OpcionForm(self.request.user, instance = opcion) #esta un objeto en instance para rellenar
        contexto={
            'form': forma #diccionario de formas
        }
        return render(request,self.template_name, contexto)

    def post(self, request, pk):
        opcion = get_object_or_404(Opcion, pk=pk)
        forma = OpcionForm(self.request.user, request.POST, instance=opcion)
        if not forma.is_valid():
            contexto = {
                'form': forma
            }
            return render(request,self.template_name, contexto)
        forma.save()
        return redirect(self.success_url)

class OpcionEliminaView(LoginRequiredMixin, DeleteView):
    model = Opcion
    success_url = reverse_lazy("encuestas:index_opcion")

class OpcionDetalleView(generic.DetailView):
    model = Opcion














