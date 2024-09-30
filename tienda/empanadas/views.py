from django.shortcuts import render
from empanadas.models import Empanada
from empanadas.models import Ingredient

def empanadas(request):
    lesEmpanadas = Empanada.objects.all()
    return render(
        request,
        'empanadas/empanadas.html',
        {'empanadas' : lesEmpanadas}
    )

def ingredients(request):
    lesIngredients = Ingredient.objects.all()
    return render(
        request,
        'empanadas/ingredients.html',
        {'ingredients' : lesIngredients}
    )