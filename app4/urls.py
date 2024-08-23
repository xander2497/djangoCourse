from django.urls import path, include
from . import views

app_name = 'app4'

urlpatterns = [
    path('', views.ingresoUsuario, name='ingresoUsuario'),
    path('informacionUsuario',views.informacionUsuario,name='informacionUsuario'),
    path('cerrarSesion',views.cerrarSesion,name='cerrarSesion'),
    path('ejemploJs',views.ejemploJs,name='ejemploJs'),
    path('crearPublicacion',views.crearPublicacion,name='crearPublicacion'),
    path('devolverDatos',views.devolverDatos,name='devolverDatos'),
    path('devolverUsuario',views.devolverUsuario,name='devolverUsuario'),
    path('devolverPub',views.devolverPub,name='devolverPub'),
    path('eliminarPub/<str:idPub>',views.eliminarPub,name='eliminarPub'),
    path('publicarComentario',views.publicarComentario,name='publicarComentario'),
    path('descargarReporte',views.descargarReporte,name='descargarReporte'),
    path('reactjs',views.reactjs,name='reactjs')
]