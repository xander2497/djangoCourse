from django.urls import path, include
from . import views

app_name = 'app2'

urlpatterns = [
    path('', views.inicio, name='inicio'),
]