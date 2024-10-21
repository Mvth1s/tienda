from django.shortcuts import render
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition

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
    
def empanada(request, empanada_id):
    # Récupérer la empanada spécifique
    laEmpanada = Empanada.objects.get(idEmpanada=empanada_id)
    
    # Récupérer la composition associée (les ingrédients et leurs quantités)
    composition = Composition.objects.filter(empanada=empanada_id)
    
    # Créer une liste des ingrédients avec leurs détails
    ingredients_list = []
    for compo in composition:
        ingredient_data = {
            'idComposition': compo.idComposition,
            'nomIngredient': compo.ingredient.nomIngredient,
            'quantite': compo.quantite
        }
        ingredients_list.append(ingredient_data)
    
    # Passer l'empanada et la liste des ingrédients au template
    return render(
        request,
        'empanadas/empanada.html',
        {
            'empanada': laEmpanada,
            'ingredients': ingredients_list
        }
    )