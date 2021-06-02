from django.urls import path
from . import views
## http://XXXXX.pythonanywhere.com.encuestas/ (index)
## http://XXXXX.pythonanywhere.com.encuestas/<id> (detalle)
## http://XXXXX.pythonanywhere.com.encuestas/<id>/votar (votar)
## http://XXXXX.pythonanywhere.com.encuestas/<id>/resultados (resultados)

## http://xxxx.pythonanywhere.com/encuestas/2
app_name='encuestas'
urlpatterns = [
    path ('',views.index, name="index"),
    # http://xxxxx.pythonanywhere.com/encuestas/5
    path('<int:id_pregunta>', views.detalle, name='detalle'),
    # http://xxxxx.pythonanywhere.com/encuestas/<id>/votar
    path('<int:id_pregunta>/votar', views.votar, name='votar'),
    # http://xxxxx.pythonanywhere.com/encuestas/<id>/resultados
    path('<int:id_pregunta>/resultados', views.resultados, name='resultados'),
]