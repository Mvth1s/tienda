from django.shortcuts import render
from empanadas.models import Empanada

def empanadas(request):
    lesEmpanadas = Empanada.objects.all()
    return render(
        request,
        'empanadas/empanadas.html',
        {'empanadas' : lesEmpanadas}
    )