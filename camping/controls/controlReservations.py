from ..models import *


def getCarpDisponibles(carpa, f_ini, f_fin):
    reservas = cant_carpas.objects.filter( carpa = carpa ).values('reserva')


    print(reservas)

    return reservas






