from django.urls import path
from . import views
app_name = 'votaciones'
urlpatterns = [
    path('', views.index, name='index'),
    path('ediciones/<int:año>/', views.detalle_edicion, name='detalle_edicion'),
    path('categorias/', views.lista_categorias, name='categorias'),
    path('categorias/<int:categoria_id>/', views.detalle_categoria, name='detalle_categoria'),
    path('votaciones/<int:votacion_id>/votar/', views.registrar_voto, name='registrar_voto'),
    path('contacto/', views.contacto, name='contacto'),
]
