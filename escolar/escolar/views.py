from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Carrera, Materia
from django.urls import reverse, reverse_lazy #funciones, clases
from django.views import generic, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CarreraForm, MateriaForm
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
class IndexView(generic.ListView):
    # Por default la plantilla seria pregunta_list.html
    template_name="escolar/index.html"
    # Por default la variable con la lista de objetos se llamaria carrera_list
    context_object_name="lista_carreras_recientes"

    def get_queryset(self):
        return Carrera.objects.all()


class DetalleView(generic.DetailView):
    # Por default la pantilla se llamaria pregunta.detail.html
    # Por default la variable en la plantilla se llamaria pregunta
    template_name="escolar/detalle.html"
    model=Carrera

#Esta vista permitr reistrarse para una carrera
#URL: http://xxxx.pythonanywhere.com/carrera/<id>/registro

#@login_required
def registro(request, id_carrera):
    m=get_object_or_404(Carrera, pk=id_carrera)
    try:
         materia_sel = m.materia_set.get(pk=request.POST['materia'])
    except(Materia.DoesNotExist, KeyError ):
        contexto ={
            'carrera' : p,
            'mensaje_error': 'Debes seleccionar una materia valida'
        }
        return render(request, 'escolar/detalle.html', contexto)
    else:
        materia_sel.num_registro += 1
        materia_sel.save()
        #solicitar al cliente que cargue otra pagina(redireccion)
        return HttpResponseRedirect(reverse('escolar:registros', args=(p.id,)))

class RegistrosView( generic.DetailView):
    # Por default la pantilla se llamaria carrera.detail.html
    # Por default la variable en la plantilla se llamaria carrera
    template_name="escolar/registros.html"
    model=Carrera

class CarreraCreaView(LoginRequiredMixin, View):
    template_name="escolar/carrera_form.html"
    success_url=reverse_lazy("escolar:index")
    def get(self, request):
        forma = CarreraForm()
        contexto={
            'form': forma #diccionario de formas
        }
        return render(request,self.template_name, contexto)

    def post(self, request):
        forma = CarreraForm(request.POST)
        if not forma.is_valid():
            contexto = {
                'form': forma
            }
            return render(request,self.template_name, contexto)
        carrera = forma.save(commit=False)
        carrera.creador = self.request.user
        carrera.save()
        return redirect(self.success_url)

class CarreraEditaView(LoginRequiredMixin, UpdateView):
    model= Carrera
    success_url = reverse_lazy("escolar:index")
    fields = ('clave_carrera',)


class CarreraEliminaView(LoginRequiredMixin, DeleteView):
    model= Carrera
    success_url = reverse_lazy("escolar:index")

class MateriaIndexView(generic.ListView):
    model = Materia
    paginate_by = 5

class MateriaCreaView(LoginRequiredMixin, View):
    template_name="escolar/materia_form.html"
    success_url=reverse_lazy("escolar:index_materia")
    def get(self, request):
        forma = MateriaForm(self.request.user)
        contexto={
            'form': forma #diccionario de formas
        }
        return render(raequest,self.template_name, contexto)

    def post(self, request):
        forma = MateriaForm(self.request.user, request.POST)
        if not forma.is_valid():
            contexto = {
                'form': forma
            }
            return render(request,self.template_name, contexto)

        return redirect(self.success_url)

class MateriaEditaView(LoginRequiredMixin, View):
    template_name="escolar/materia_form.html"
    success_url=reverse_lazy("escolar:index_materia")
    def get(self, request, pk):
        materia = get_object_or_404(Materia, pk=pk) #primer pk llave primaria, segundo pk lo que recibo
        forma = MateriaForm(self.request.user, instance = materia) #esta un objeto en instance para rellenar
        contexto={
            'form': forma #diccionario de formas
        }
        return render(request,self.template_name, contexto)

    def post(self, request, pk):
        materia = get_object_or_404(Materia, pk=pk)
        forma = MateriaForm(self.request.user, request.POST, instance=materia)
        if not forma.is_valid():
            contexto = {
                'form': forma
            }
            return render(request,self.template_name, contexto)
        forma.save()
        return redirect(self.success_url)

class MateriaEliminaView(LoginRequiredMixin, DeleteView):
    model = Materia
    success_url = reverse_lazy("escolar:index_materia")

class MateriaDetalleView(generic.DetailView):
    model = Materia