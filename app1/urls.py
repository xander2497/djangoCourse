from django.urls import path, include
from . import views

app_name = 'app1'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevaRuta', views.nuevo, name='nuevo'),
    path('welcome', views.welcome, name='welcome'),
]