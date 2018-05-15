from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    if request.method == 'POST':
        #getting values from post
        user = request.POST.get('username')
        passwd = request.POST.get('pass')
        template = loader.get_template('show.html')
        context = {
            'User': user,
            'Paswd': passwd[::-1]
        }
        return HttpResponse(template.render(context,request))
    else:
        template = loader.get_template('SistLogin/index.html')
        return HttpResponse(template.render(None,request))