from django import forms
from django.forms import ModelForm
from empanadas.models import Ingredient
from empanadas.models import Empanada
from empanadas.models import Composition

# classe permettant de faire le fomulaire de création d'un ingrédient
class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']
        

# from django import forms
# class IngredientForm(forms.Form):
#     nomIngredient = forms.charField(label = 'nomIngredient', max_length = 50)

# classe permettant de faire le formulaire de création d'un empanada
class EmpanadaForm(ModelForm):
    class Meta:
        model = Empanada
        fields = ['nomEmpanada', 'prix']
        

# Classe permettant de faire l'ajout des ingrédients dans une empanada
class CompositionForm(ModelForm):
    class Meta:
        model = Composition
        fields = ['ingredient', 'quantite']
        