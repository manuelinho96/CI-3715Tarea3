from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.template import loader
from .models import Seguridad

# Iniciamos la clase seguridad
SeguridadClass = Seguridad()

# Vista del registro
def registro(request):
    if request.method == 'POST':
        #getting values from post
        user = request.POST.get('username')
        passwd = request.POST.get('pass')
        passwd2 = request.POST.get('pass2')
        validarRegistro = SeguridadClass.registrarUsuario(user, passwd, passwd2)
        # Verifico que los datos del usuario para registro son correctos
        if validarRegistro[0] == 0:
            # Me dirijo al login con el mensaje de exito
            messages.success(request, validarRegistro[1])
            return  HttpResponseRedirect('login')
        else:
            # Rerijo a la pagina de registro con el mensaje de error correspondiente
            messages.info(request, validarRegistro[1])
            return  HttpResponseRedirect('registro')
    else:
        # Renderizo el index
        template = loader.get_template('SistLogin/index.html')
        return HttpResponse(template.render(None,request))

# Vista del login
def login(request):
    if request.method == 'POST':
        #getting values from post
        user = request.POST.get('username')
        passwd = request.POST.get('pass')
        validarRegistro = SeguridadClass.IngresarUsuario(user, passwd)
        # Verifico que el usuario y la clave pueden iniciar sesion
        if validarRegistro[0] == 0:
            # Redirijo al menu con un mensaje de exito
            messages.success(request, validarRegistro[1])
            return HttpResponseRedirect('menu')
        else:
            # Redirijo de nuevo al login con un mensaje de error
            messages.info(request, validarRegistro[1])
            return  HttpResponseRedirect('login')
    else:
        # Renderizo el inicio de sesion
        template = loader.get_template('SistLogin/iniciosesion.html')
        return HttpResponse(template.render(None,request))
    
def menu(request):
    template = loader.get_template('SistLogin/menu.html')
    return HttpResponse(template.render(None,request))