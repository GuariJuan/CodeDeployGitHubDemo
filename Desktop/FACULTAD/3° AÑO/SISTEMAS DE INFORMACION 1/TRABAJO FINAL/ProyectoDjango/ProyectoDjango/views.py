from django.http import HttpResponse
import datetime
from django.template import Template,Context
#from django.template import loader
from django.shortcuts import render
class Persona(object):
    
    def __init__(self, nombre, apellido):
    
        self.nombre=nombre
        self.apellido=apellido
   
    

def saludo(request): # primera vista

    p1=Persona("Profesor Juan","Diaz")

    #nombre="Juan"
    
    #apellido="Diaz"

    temas_del_curso=["Plantillas","Modelos","Formularios","Vistas","Despliegue"]

    ahora=datetime.datetime.now()
    
    #doc_externo=open("C:/Users/CQ43/Desktop/FACULTAD/3° AÑO/SISTEMAS DE INFORMACION 1/TRABAJO FINAL/ProyectoDjango/ProyectoDjango/Plantillas/miPlantillas.html")
    
    #plt=Template(doc_externo.read())

    #doc_externo.close()

    #doc_externo=loader.get_template('miPlantilla.html')
    
    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})

    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})
    
    return render(request, "miPlantilla.html", {"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temas_del_curso})



def cursoC(request):

    fecha_actual=datetime.datetime.now()

    return render(request,"cursoC.html",{"dameFecha":fecha_actual})


def despedida(request):
    return HttpResponse("Hasta luego")


def dameFecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento="""<html>
    <body>
    <h2>
    FECHA Y HORA ACTUALES %s
    </h2>
    </body>
    </html>"""% fecha_actual

    return HttpResponse(documento)

def calcularEdad(request,edad, anio):
    #edadActual=18
    periodo=anio-2020
    edadFutura=edad+periodo
    documento="<html><body><h2>En el año %s tendras %s años</h2></body></html>"%(anio,edadFutura)
    return HttpResponse(documento)