from django.forms import ModelForm
from empanadas.models import Ingredient
from empanadas.models import Empanada

class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ['nomIngredient']
        

# from django import forms
# class IngredientForm(forms.Form):
#     nomIngredient = forms.charField(label = 'nomIngredient', max_length = 50)

class EmpanadaForm(ModelForm):
    class Meta:
        model = Empanada
        fields = ['nomEmpanada', 'prix']
        