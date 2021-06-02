from django.urls import path
from .import views
## http://XXXXX.pythonanywhere.com.encuestas/ (index)
## http://XXXXX.pythonanywhere.com.encuestas/<id> (detalle)
## http://XXXXX.pythonanywhere.com.encuestas/<id>/votar (votar)
## http://XXXXX.pythonanywhere.com.encuestas/<id>/resultados (resultados)

## http://xxxx.pythonanywhere.com/encuestas/2
app_name='encuestas'
urlpatterns = [
    path ('',views.IndexView.as_view(), name="index"),
    # http://xxxxx.pythonanywhere.com/encuestas/5
    path('<int:pk>', views.DetalleView.as_view(), name='detalle'),
    # http://xxxxx.pythonanywhere.com/encuestas/<id>/votar
    path('<int:id_pregunta>/votar', views.votar, name='votar'),
    # http://xxxxx.pythonanywhere.com/encuestas/<id>/resultados
    path('<int:pk>/resultados', views.ResultadosView.as_view(), name='resultados'),
    # http://xxxxx.pythonanywhere.com/encuestas/crear
    path('crear', views.PreguntaCreaView.as_view(), name='crear'),
    # http://xxxxx.pythonanywhere.com/encuestas/<id>/editar
    path('<int:pk>/editar', views.PreguntaEditaView.as_view(), name='editar'),
    # http://xxxxx.pythonanywhere.com/encuestas/<id>/eliminar
    path('<int:pk>/eliminar', views.PreguntaEliminaView.as_view(), name='eliminar'),
      # http://xxxxx.pythonanywhere.com/encuestas/opciones
    path ('opciones',views.OpcionIndexView.as_view(), name="index_opcion"),
    path('opciones/crear', views.OpcionCreaView.as_view(), name='crea_opcion'),
    path('opciones/<int:pk>', views.OpcionDetalleView.as_view(), name='detalle_opcion'),
    path('opciones/<int:pk>/editar', views.OpcionEditaView.as_view(), name='editar_opcion'),
    path('opciones/<int:pk>/eliminar', views.OpcionEliminaView.as_view(), name='eliminar_opcion')

]