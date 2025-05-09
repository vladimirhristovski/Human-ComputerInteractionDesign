from datetime import datetime

from django.shortcuts import render

from .models import Flight


def index(request):
    flights = Flight.objects.filter(date__lte=datetime.now().date())
    context = {'flight_list': flights, 'app_name': 'FlightApp'}
    return render(request, 'index.html', context)


def details(request, flight_id):
    flight = Flight.objects.filter(id=flight_id).first()
    context = {'flight_data': flight, 'app_name': 'FlightApp'}
    return render(request, 'details.html', context)
