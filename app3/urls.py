from django.urls import path, include
from . import views

app_name = 'app3'

urlpatterns = [
    path('', views.directorio, name='directorio'),
    path('nuevoRegistro',views.nuevoRegistro,name='nuevoRegistro'),
    path('nuevoDepartamento',views.nuevoDepartamento,name='nuevoDepartamento'),
    path('vistaDepartamento/<str:idDepartamento>',views.vistaDepartamento,name='vistaDepartamento'),
    path('vistaUsuario/<str:idPersona>',views.vistaUsuario,name='vistaUsuario')
]