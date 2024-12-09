from django.shortcuts import render, redirect
from empanadas.models import Empanada
from empanadas.models import Ingredient
from empanadas.models import Composition
from empanadas.forms import IngredientForm
from empanadas.forms import EmpanadaForm
from empanadas.forms import CompositionForm
from django.contrib.auth.models import User
from comptes.models import TiendaUser


def empanadas(request):
    user = None
    if request.user.is_authenticated:
        user = TiendaUser.objects.get(id = request.user.id)
    lesEmpanadas = Empanada.objects.all()
    return render(
        request,
        'empanadas/empanadas.html',
        {'empanadas' : lesEmpanadas,
        'user': user,}
    )

def ingredients(request):
    user = None
    if request.user.is_staff:
        lesIngredients = Ingredient.objects.all()
        user = User.objects.get(id = request.user.id)
        return render(
            request,
            'empanadas/ingredients.html',
            {'ingredients' : lesIngredients, 'user' : user,}
    )
    elif request.user.is_authenticated:
        return redirect ('/empanadas')
    else:
        return redirect('/login')
    
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
    user = None
    if request.user.is_staff:
        form = IngredientForm(request.POST)
        user = User.objects.get(id = request.user.id)
        if form.is_valid():
            nomIngr = form.cleaned_data['nomIngredient']
            ingr = Ingredient()
            ingr.nomIngredient = nomIngr
            ingr.save()
            return render(
            request,
            'empanadas/traitementFormulaireCreationIngredient.html',
            {'nom' : nomIngr , 'user':user},
        )
        else:
            return render(
            request, 'empanadas/formulaireNonValide.html',{'erreurs' : form.errors, 'user':user},
        )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else:
        return redirect('/login')
    
def formulaireCreationIngredient(request):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        return render(
        request,
        'empanadas/formulaireCreationIngredient.html', {'user':user}
    )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else:
        return redirect('/login')
    
def creerEmpanada(request):
    user = None
    if request.user.is_staff:
        form = EmpanadaForm(request.POST)
        user = User.objects.get(id = request.user.id)
        if form.is_valid():
            nomEmp = form.cleaned_data['nomEmpanada']
            prixEmp = form.cleaned_data['prix']
            emp = Empanada()
            emp.nomEmpanada = nomEmp
            emp.prix = prixEmp
            emp.image = request.FILES['image']
            emp.save()
            return render(
                request,
                'empanadas/traitementFormulaireCreationEmpanada.html',
                {'nom' : nomEmp, 'prix' : prixEmp, 'user' : user},
            )
        else:
            return render(
            request, 'empanadas/formulaireNonValide.html',{'erreurs' : form.errors},
        )
    elif request.user.is_authenticated:
        return redirect('/empanadas')
    else:
        return redirect('/login')
    
def formulaireCreationEmpanada(request):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        return render(
        request,
        'empanadas/formulaireCreationEmpanada.html', {'user':user}
    )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
    
def ajouterIngredientDsEmpanada(request, empanada_id):
    user = None
    if request.user.is_staff:
        form = CompositionForm(request.POST)
        user = User.objects.get(id = request.user.id)
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
            return redirect('/empanada/%d/' % empanada_id, {'user':user})  # Redirigez vers la page de détail de l'empanada
        else:
            return render(
                request,
                'empanadas/formulaireNonValide.html',
            {'erreurs': form.errors},
        )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
        
def supprimerEmpanada(request, empanada_id):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        # Récupérer l'empanada à supprimer
        empanada = Empanada.objects.get(idEmpanada = empanada_id)
        # Supprimer l'empanada
        empanada.delete()
        # Redirection vers la liste des empanadas
        return redirect('liste_empanadas', {'user':user})
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
    
def afficherFormulaireModificationEmpanada(request, empanada_id):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        emp = Empanada.objects.get(idEmpanada = empanada_id)
        return render(
            request,
        'empanadas/formulaireModificationEmpanada.html',
        { 'empanada' : emp, 'user':user }
        )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
    
def modifierEmpanada(request, empanada_id):
    user = None
    if request.user.is_staff:
        emp = Empanada.objects.get(idEmpanada = empanada_id)
        user = User.objects.get(id = request.user.id)
        form = EmpanadaForm(request.POST, request.FILES, instance = emp)
        if form.is_valid():
            # Mettre à jour l'empanada dans la base de données
            form.save()
            # Rediriger vers la liste des empanadas
            return redirect('liste_empanadas', {'user':user})
        else:
            # Le formulaire n'est pas valide, afficher les erreurs
            return render(
                request,
            'empanadas/formulaireNonValide.html',
            { 'erreurs': form.errors },
        )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
    
def supprimerIngredient(request, ingredient_id):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        # Récupérer l'ingredient à supprimer
        ingredients = Ingredient.objects.get(idIngredient = ingredient_id)
        # Supprimer l'ingredient
        ingredients.delete()
        # Redirection vers la liste des ingredients
        return redirect('liste_ingredients', {'user':user})
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
    
def afficherFormulaireModificationIngredient(request, ingredient_id):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        ing = Ingredient.objects.get(idIngredient = ingredient_id)
        return render(
            request,
        'empanadas/formulaireModificationIngredient.html',
        { 'ingredient' : ing , 'user':user}
        )
    elif request.user.is_authenticated:
        return redirect('/empandas')
    else: return redirect('/login')
    
def modifierIngredient(request, ingredient_id):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
        ing = Ingredient.objects.get(idIngredient = ingredient_id)
        form = IngredientForm(request.POST, instance = ing)
        if form.is_valid():
            # Mettre à jour l'ingredient dans la base de données
            form.save()
            # Rediriger vers la liste des ingredient
            return redirect('liste_ingredients', {'user': user})
        else:
            # Le formulaire n'est pas valide, afficher les erreurs
            return render(request, 'empanadas/formulaireModificationIngredient.html', {'form': form, 'ingredient': ing, 'user':user})
    elif request.user.is_authenticated:
        return redirect('/empanadas')
    else: return redirect('/login')
    
def supprimerIngredientDansEmpanada(request, empanada_id, ligne_id):
    user = None
    if request.user.is_staff:
    # Récupérer la composition à supprimer
        user = User.objects.get(id = request.user.id)
        comp = Composition.objects.get(idComposition = ligne_id)
        comp.delete()

        # Récupérer l'empanada associée
        emp = Empanada.objects.get(idEmpanada = empanada_id)

        # Rediriger vers la page de détail de l'empanada
        return redirect('detail_empanada', empanada_id = emp.idEmpanada)
    elif request.user.is_authenticated:
        return redirect('/empanadas')
    else:
        return redirect('/login')
    
def modifierIngredientDansEmpanada(request, empanada_id, ligne_id):
    user = None
    if request.user.is_staff:
        user = User.objects.get(id = request.user.id)
    # Récupérer la composition à modifier
        comp = Composition.objects.get(idComposition = ligne_id)
        # Récupérer la nouvelle quantité depuis le formulaire
        quantite = request.POST.get('quantite')
        # Mettre à jour la quantité dans la composition
        comp.quantite = quantite
        comp.save()  # Enregistrez les modifications
        # Récupérer l'empanada associée
        emp = Empanada.objects.get(idEmpanada = empanada_id)
        # Rediriger vers la page de détail de l'empanada
        return redirect('detail_empanada', empanada_id = emp.idEmpanada)
    elif request.user.is_authenticated:
        return redirect('/empanadas')
    else:
        return redirect('/login')