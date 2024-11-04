from django.shortcuts import render, redirect
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition
from empanadas.forms import IngredientForm
from empanadas.forms import EmpanadaForm
from empanadas.forms import CompositionForm


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
    # Récupérer l'empanada spécifique
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
    
    # Récupérer tous les ingrédients pour le formulaire de sélection
    all_ingredients = Ingredient.objects.all()
    
    # Créer une instance du formulaire CompositionForm
    form = CompositionForm()
    
    # Passer l'empanada, la liste des ingrédients et le formulaire au template
    return render(
        request,
        'empanadas/empanada.html',
        {
            'empanada': laEmpanada,
            'ingredients': ingredients_list,
            'all_ingredients': all_ingredients,
            'form': form  # Passer le formulaire au template
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
    
def ajouterIngredientDsEmpanada(request, empanada_id):
    form = CompositionForm(request.POST)
    if form.is_valid():
        ingr = form.cleaned_data['ingredient']
        qt = form.cleaned_data['quantite']

        # Vérifiez si l'ingrédient est déjà présent dans l'empanada
        ligne_existante = Composition.objects.filter(
            empanada_id=empanada_id,
            ingredient=ingr
        ).first()  # Utilisez .first() pour obtenir l'instance ou None

        if ligne_existante:  # Si l'ingrédient existe déjà
            ligne_existante.quantite += qt  # Mettez à jour la quantité
            ligne_existante.save()  # Sauvegardez les modifications
        else:
            # Créez une nouvelle ligne pour la composition
            ligne = Composition()
            ligne.ingredient = ingr
            ligne.empanada_id = empanada_id  # Associez à l'empanada par son ID
            ligne.quantite = qt
            ligne.save()  # Sauvegardez la nouvelle ligne

        return redirect('/empanada/%d/' % empanada_id)  # Redirigez vers la page de détail de l'empanada

    else:
        return render(
            request,
            'empanadas/formulaireNonValide.html',
            {'erreurs': form.errors},
        )
        
def supprimerEmpanada(request, empanada_id):
    # Récupérer l'empanada à supprimer
    empanada = Empanada.objects.get(idEmpanada = empanada_id)
    # Supprimer l'empanada
    empanada.delete()
    # Redirection vers la liste des empanadas
    return redirect('liste_empanadas')
    
def afficherFormulaireModificationEmpanada(request, empanada_id):
    emp = Empanada.objects.get(idEmpanada = empanada_id)
    return render(
        request,
        'empanadas/formulaireModificationEmpanada.html',
        { 'empanada' : emp }
    )
    
def modifierEmpanada(request, empanada_id):
    emp = Empanada.objects.get(idEmpanada = empanada_id)
    form = EmpanadaForm(request.POST, instance = emp)
    if form.is_valid():
        # Mettre à jour l'empanada dans la base de données
        form.save()
        # Rediriger vers la liste des empanadas
        return redirect('liste_empanadas')
    else:
        # Le formulaire n'est pas valide, afficher les erreurs
        return render(request, 'empanadas/formulaireModificationEmpanada.html', {'form': form, 'empanada': empanada})
    
def supprimerIngredient(request, ingredient_id):
    # Récupérer l'ingredient à supprimer
    ingredients = Ingredient.objects.get(idIngredient = ingredient_id)
    # Supprimer l'ingredient
    ingredients.delete()
    # Redirection vers la liste des ingredients
    return redirect('liste_ingredients')
    
def afficherFormulaireModificationIngredient(request, ingredient_id):
    ing = Ingredient.objects.get(idIngredient = ingredient_id)
    return render(
        request,
        'empanadas/formulaireModificationIngredient.html',
        { 'ingredient' : ing }
    )
    
def modifierIngredient(request, ingredient_id):
    ing = Ingredient.objects.get(idIngredient = ingredient_id)
    form = IngredientForm(request.POST, instance = ing)
    if form.is_valid():
        # Mettre à jour l'ingredient dans la base de données
        form.save()
        # Rediriger vers la liste des ingredient
        return redirect('liste_ingredients')
    else:
        # Le formulaire n'est pas valide, afficher les erreurs
        return render(request, 'empanadas/formulaireModificationIngredient.html', {'form': form, 'ingredient': ing})