from django.shortcuts import render
from .models import Locomotive, Brigade, Repair

def index(request):
    locomotives = Locomotive.objects.all()
    brigades = Brigade.objects.all()
    repairs = Repair.objects.all()
    return render(request, 'index.html', {
        'locomotives': locomotives,
        'brigades': brigades,
        'repairs': repairs
    })
