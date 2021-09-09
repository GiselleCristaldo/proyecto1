from django.urls import path
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index), #/desafio/
     path('<int:mes>', views.desafio_mensual_por_numero),
    path('<str:mes>', views.desafio_mensual, name= 'desafio-mensual'),
]