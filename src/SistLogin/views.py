from django.shortcuts import render
from django.http import HttpResponse
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
        template = loader.get_template('show.html')
        
        context = {
            'User': user,
            'Paswd': passwd[::-1]
        }
        return HttpResponse(template.render(context,request))
    else:
        template = loader.get_template('SistLogin/index.html')
        return HttpResponse(template.render(None,request))