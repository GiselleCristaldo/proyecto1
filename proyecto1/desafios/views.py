from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string 
# Create your views here.
desafios = {
    'enero': 'Practicar Python',
    'febrero': 'Leer un libro',
    'marzo': 'Tomar mas agua',
    'abril':'Comer mas verduras',
    'mayo': 'Comer cuatro piezas de fruta al dia',
    'junio': 'Hacer ejercicio media hora',
    'julio': 'Consumir menos azucar',
    'agosto': 'Evitar comidas fritas',
    'septiembre': 'Dormir 8 horas diarias',
    'octubre': 'Evitar bebidas con gas',
    'noviembre': 'Reducir el uso de plasticos',
    'diciembre': 'No usar bolsas',
}


def desafio_mensual(request, mes):
    texto_desafio = ''
    try: 
        texto_desafio = desafios[mes]
    except:
        return HttpResponseNotFound('Mes no implementado')
    return HttpResponse (texto_desafio)

def desafio_mensual_por_numero(request, mes):
    lista_meses = list(desafios.keys())
    if mes > 12: 
        return HttpResponseNotFound('Mes no encontrado. Pruebe utilizando un numero del 1 al 12')
    else:
         return HttpResponseRedirect(lista_meses[mes-1])
    return HttpResponseRedirect (lista_meses[mes-1])
