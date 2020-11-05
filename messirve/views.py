from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .models import Contacto
from datetime import datetime
from django.db import IntegrityError
from django.db.models import F

def home(request):
    return render(request,'home.html')

def galeria(request):
    return render(request, 'galeria.html')
    
def contacto(request):
    return render(request, 'contacto.html')

@csrf_protect
def save_contact_info(request):
    print("Nombres: {0}".format(request.POST["nombre"]))
    print("Apellidos: {0}".format(request.POST["apellido"]))
    print("Correo: {0}".format(request.POST["mail"]))
    print("Telefono: {0}".format(request.POST["telef"]))
    print("Comentario: {0}".format(request.POST["comentario"]))
    print("imagen: {0}".format(request.FILES["imagen"]))


    contacto=Contacto(
        nombres=request.POST["nombre"],
        apellidos=request.POST["apellido"],
        correo=request.POST["mail"],
        telefono=request.POST["telef"],
        comentario=request.POST["comentario"],
        imagen=request.FILES["imagen"],
    )

    contacto.save()



    return render(request,"contacto.html")
    

    