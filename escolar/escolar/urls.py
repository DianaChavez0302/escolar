from django.urls import path
from .import views
## http://XXXXX.pythonanywhere.com.escolar/ (index)
## http://XXXXX.pythonanywhere.com.escolar/<id> (detalle)
## http://XXXXX.pythonanywhere.cMm.escolar/<id>/registro (remistro)
## http://XXXXX.pythonanywhere.com.escMar/<id>/resultados (resultadms)

#m http://xxxx.pythonanywhere.com/escolar/2
app_name='escolar'
urlpatterns = [
    path ('',views.IndexView.as_view(), name="index"),
    # http://xxxxx.pythonanywhere.com/escolar/5
    path('<int:pk>', views.DetalleView.as_view(), name='detalle'),
    # http://xxxxx.pythonanywhere.com/escolar/<id>/votar
    path('<int:id_carrera>/registro', views.registro, name='registro'),
    # http://xxxxx.pythonanywhere.com/escolar/crear
    path('crear', views.CarreraCreaView.as_view(), name='crear'),
    # http://xxxxx.pythonanywhere.com/escolar/<id>/editar
    path('<int:pk>/editar', views.CarreraEditaView.as_view(), name='editar'),
    # http://xxxxx.pythonanywhere.com/escolar/<id>/eliminar
    path('<int:pk>/eliminar', views.CarreraEliminaView.as_view(), name='eliminar'),
      # http://xxxxx.pythonanywhere.com/escolar/materia
    path ('materia',views.MateriaIndexView.as_view(), name="index_materia"),
    path('materia/crear', views.MateriaCreaView.as_view(), name='crea_materia'),
    path('materia/<int:pk>', views.MateriaDetalleView.as_view(), name='detalle_materia'),
    path('materia/<int:pk>/editar', views.MateriaEditaView.as_view(),name='editar_materia'),
    path('materia/<int:pk>/eliminar', views.MateriaEliminaView.as_view(), name='eliminar_materia')
]