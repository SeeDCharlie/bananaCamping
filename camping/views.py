from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .models import *

def index(request):
    return render(request, 'camping/index.html')

def about(request):
    return render(request, 'camping/about.html')
def services(request):
    return render(request, 'camping/services.html')

def reservations(request):
    return render(request, 'camping/reservations.html')

def contact(request):
    return render(request, 'camping/contact.html')

def getContactForm(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' and request.method == 'POST':
        dats = json.loads(request.POST.get('dats'))
        try:
            peticion = contact_request(nombre = dats['name'], no_celular = dats['cell'],email = dats['email'], mensaje = dats['message'] )
            peticion.save()
            return JsonResponse({'success': True, 'msj': 'Su solicitud sera atendida pronto'})
        except Exception as error : 
            print(error)
            return JsonResponse({'success': False, 'msj': 'No pudimos procesar la solicitus \n error: %s.'%error})

    return redirect('solicitud')