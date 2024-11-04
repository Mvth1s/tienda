from django.shortcuts import render
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition
from empanadas.forms import IngredientForm
from empanadas.forms import EmpanadaForm


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
    
def creerIngredient(request):
    form = IngredientForm(request.POST)
    if form.is_valid():
        nomIngr = form.cleaned_data['nomIngredient']
        ingr = Ingredient()
        ingr.nomIngredient = nomIngr
        ingr.save()
        return render(
            request,
            'empanadas/traitementFormulaireCreationIngredient.html',
            {'nom' : nomIngr },
        )
    
def formulaireCreationIngredient(request):
    return render(
        request,
        'empanadas/formulaireCreationIngredient.html'
    )
    
def creerEmpanada(request):
    form = EmpanadaForm(request.POST)
    if form.is_valid():
        nomEmp = form.cleaned_data['nomEmpanada']
        prixEmp = form.cleaned_data['prix']
        emp = Empanada()
        emp.nomEmpanada = nomEmp
        emp.prix = prixEmp
        emp.save()
        return render(
            request,
            'empanadas/traitementFormulaireCreationEmpanada.html',
            {'nom' : nomEmp, 'prix' : prixEmp },
        )
    
def formulaireCreationEmpanada(request):
    return render(
        request,
        'empanadas/formulaireCreationEmpanada.html'
    )