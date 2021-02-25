from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('about/', about,  name = 'about'),
    path( 'services/', services, name = 'services'),
    path('reservations', reservations, name = 'reservations'),
    path('contact/', contact, name = 'contact'),
    path('getContactForm/', getContactForm, name = 'getContactForm'),
]