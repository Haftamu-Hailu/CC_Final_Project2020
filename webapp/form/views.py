from django.http import HttpResponse
from django.shortcuts import render
from form.models import Simulator


def home(request):
    return render(request, 'index.html')


def simulatorSetUp(request):
    simulator = Simulator()
    status = simulator.get_initial_data(request.POST)
    return HttpResponse('', status=status)

