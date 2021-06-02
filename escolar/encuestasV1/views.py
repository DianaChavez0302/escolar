from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Pregunta, Opcion
from django.template import loader
from django.urls import reverse


# Create your views here.
def index(request):
    lista_preguntas=Pregunta.objects.order_by('-fecha_pub')[:10]
    #plantilla = loader.get_template('encuestas/index.html')
    contexto ={
        'lista_preguntas_recientes': lista_preguntas
    }
    #return HttpResponse(plantilla.render(contexto, request))
   # resultado=",".join([p.texto_pregunta for p in lista_preguntas] )
    #return HttpResponse(resultado)
    return rendeer (request, 'encuestas/index.html', contexto)


def detalle(request, id_pregunta):
   # try:
    #    pregunta=Pregunta.objects.get(id=id_pregunta)
    #except Pregunta.DoesNotExist:
     #   raise Http404("!la pregunta solicitada no existe!")
    #contexto={
     #   'pregunta' : p
    #}
    #return render(request, 'encuestas/detalle.html', contexto)
    p=get_object_or_404(Pregunta, pk=id_pregunta)
    contexto ={
        'pregunta':p
    }
    return render(request, 'encuestas/detalle.html', contexto)
    ##response ="estas viendo los resultados de la pregunta %s"
    ##return HttpResponse(response % id_pregunta)

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

def resultados(request, id_pregunta):
    p=get_object_or_404(Pregunta, pk=id_pregunta)
    contexto ={
        'pregunta':p
    }
    return render(request, 'encuestas/resultados.html', contexto)


