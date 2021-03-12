from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .models import *
from datetime import datetime, timedelta 
from .controls.controlReservations import *

def index(request):
    return render(request, 'camping/index.html')

def about(request):
    return render(request, 'camping/about.html')
def services(request):
    return render(request, 'camping/services.html')

def reservations(request, fecha_inicio = datetime.now().strftime("%d/%m/%y %H:%M %P") , fecha_fin = (datetime.now() + timedelta(1)).strftime("%d/%m/%y %H:%M %P"), cant_pers = 2):

    getCarpDisponibles(carpas.objects.get(pk=1), fecha_inicio, fecha_fin)

    context = {'carpas': carpas.objects.all() , 'fecha_inicio': fecha_inicio, 'fecha_fin': fecha_fin}



    print(context)
    return render(request, 'camping/reservations.html', context=context)

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