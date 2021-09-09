from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string 
from django.urls import reverse
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

def index(request):
    lista_meses = list(desafios.keys())
    meses= ''
    for mes in lista_meses:
       meses += f'<li><a href="{mes}">{mes}</a></li>'
    return HttpResponse("""<h1>Aplicacion Desafios</h1>"""
    f'<ul>{meses}</ul>')

    

def desafio_mensual(request, mes):
    texto_desafio = ''
    try: 
        texto_desafio = desafios[mes]
    except:
        return HttpResponseNotFound(f'<strong>(Mes no implementado)</strong>')
    return HttpResponse (f'<h1>{texto_desafio}</h1>')

def desafio_mensual_por_numero(request, mes):
    lista_meses = list(desafios.keys())

    # reverse_path = reverse('desafio-mensual', args=[])
    # print('reverse_path', reverse_path)

    if mes > 12: 
        return HttpResponseNotFound(f'<strong>(Mes no encontrado. Pruebe utilizando un numero del 1 al 12)</strong>')
    else:
         return HttpResponseRedirect(lista_meses[mes-1])
    return HttpResponseRedirect (lista_meses[mes-1])
