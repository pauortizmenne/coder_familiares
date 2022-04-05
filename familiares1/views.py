from django.shortcuts import render
from django.template import loader
from .models import Familia
from django.http import HttpResponse

# Create your views here.


def listado_familiares(request):
   
    template = loader.get_template('listado_familiares.html')
    familiares=Familia.objects.all()
    print(familiares)
    context = {
        'familiares': familiares,
    }
    return HttpResponse(template.render(context, request))