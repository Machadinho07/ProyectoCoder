from  django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

hora = datetime(2022, 8, 18, 23)#fecha exacta

Mensaje = 'Hola, esto es un mensjae simple'

Dreams = {
        'Fase1':'Terminar Estudios''Conseguir Trabajo',
        'Fase2':'Aprender todo el oficio''Ser autonomo'
}


def mensajito(request):
    template = loader.get_template('plantilla2.html')

    Mensajon = 'HOOOLA'

    mensajito = {

        'Mensaje':'Holandaa!',
        'Mensaje2':Mensajon,
        'Mensaje3':Dreams
    }

    documento = template.render(mensajito)

    return HttpResponse(documento)



def probando_plantilla(request):

    plantilla = loader.get_template('plantillas.html')



    galleta = {
        'sabor':'dulce',
        'calidad':'intermedia',
        'dato3': hora,
        'precio':'nashei',
        'Mensaje': Mensaje

    }

    documento = plantilla.render(galleta)

    return HttpResponse(documento)


def saludo(request):
    now = datetime.now()
    return HttpResponse (f'Hola, Bienvenido! son las {now} ')

def mi_nombre(request, nombre):

    text_response = f"tu nombre es {nombre}"
    return HttpResponse(text_response)
