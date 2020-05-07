from django.shortcuts import render
from form.models import Simulator
from simulator.main import start_simulation


def home(request):
    return render(request, 'index.html')


def simulatorSetUp(request):
    simulator = Simulator()
    initial_data = simulator.get_initial_data(request.POST)
    status, results = start_simulation(initial_data)
    return render(request, 'index.html', {'items': results})

