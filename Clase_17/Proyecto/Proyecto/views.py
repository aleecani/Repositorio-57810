from django.template import Template, Context
from django.http import HttpResponse

def saludar(request):
    saludo = "Bienvenidos a la comision 57810 - Clase Django"
    return HttpResponse(saludo) 

def bienvenido(request,nombre,apellido):
    saludo = f"Te damos la bienvenida a la comision 57810 {apellido}, {nombre}"
    return HttpResponse(saludo)   

def bienvenido_html(request,nombre,apellido):
    saludo = f"""
    <html>
    <h1>Bienvenidos al curso de Django!<h1>
    <h2>Te damos la bienvenida {apellido}, {nombre}<h2>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    with open("C:/CoderHouse/57810/Clase_17/Proyecto/Proyecto/plantillas/bienvenido.html") as miHtml:
        plantilla = Template(miHtml.read())
        contexto = Context()
        saludo = plantilla.render(contexto)
    return HttpResponse(saludo)