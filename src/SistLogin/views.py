from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template import loader
from .models import Seguridad

# Iniciamos la clase seguridad
SeguridadClass = Seguridad()

# Create your views here.
def index(request):
    if request.method == 'POST':
        #getting values from post
        user = request.POST.get('username')
        passwd = request.POST.get('pass')
        passwd2 = request.POST.get('pass2')
        validarRegistro = SeguridadClass.registrarUsuario(user, passwd, passwd2)
        if validarRegistro[0] == 0:
            messages.success(request, validarRegistro[1])
            return  HttpResponseRedirect('login')
        else:
            messages.info(request, validarRegistro[1])
            return  HttpResponseRedirect('registro')
    else:
        template = loader.get_template('SistLogin/index.html')
        return HttpResponse(template.render(None,request))

def login(request):
    if request.method == 'POST':
        #getting values from post
        user = request.POST.get('username')
        passwd = request.POST.get('pass')
        validarRegistro = SeguridadClass.IngresarUsuario(user, passwd)
        if validarRegistro[0] == 0:
            messages.success(request, validarRegistro[1])
            return HttpResponseRedirect('menu')
        else:
            messages.info(request, validarRegistro[1])
            return  HttpResponseRedirect('logininvalido')
    else:
        template = loader.get_template('SistLogin/iniciosesion.html')
        return HttpResponse(template.render(None,request))
    
def menu(request):
    template = loader.get_template('SistLogin/menu.html')
    return HttpResponse(template.render(None,request))