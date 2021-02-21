from django.shortcuts import render

# Create your views here.


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