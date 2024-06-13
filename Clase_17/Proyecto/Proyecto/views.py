from django.template import Template, Context, loader
from django.http import HttpResponse
import datetime,random
from aplicacion.models import *


def saludar(request):
    saludo = "Bienvenidos a la comision 57810 - Clase Django"
    return HttpResponse(saludo) 

def bienvenido(request,nombre,apellido):
    saludo = f"Te damos la bienvenida a la comision 57810 {apellido}, {nombre}"
    return HttpResponse(saludo)   

def bienvenido_html(request,nombre,apellido):
    hoy = datetime.datetime.now()
    saludo = f"""
    <html>
    <h1>Bienvenidos al curso de Django!<h1>
    <h2>Te damos la bienvenida {apellido}, {nombre}<h2>
    <h3>Hoy es {hoy} <h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    with open("C:/CoderHouse/57810/Clase_17/Proyecto/Proyecto/plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)
    return HttpResponse(saludo)

#______________________________________
def bienvenido_tpl2(request):
    hoy = datetime.datetime.now()
    nombre = "Ale"
    apellido = "Cani"
    notas = [7,6,5,10,9,5]
    contexto = {"nombre": nombre, "apellido":apellido, "hoyy": hoy,
                "notas":notas}
    plantilla = loader.get_template("bienvenido_tpl.html")
    respuesta = plantilla.render(contexto)
    return HttpResponse(respuesta)

def nuevo_curso(request):
    nro_comision = random.randint(1000, 200000)
    nombrecurso = "Python " + str(nro_comision)
    curso = Curso( nombre=nombrecurso, comision=nro_comision)
    curso.save()
    respuesta = f"<html><h1>Se guardo {nombrecurso} y comision {nro_comision}<h1><html>"
    return HttpResponse(respuesta)
