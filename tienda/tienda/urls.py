from django.contrib import admin
from django.urls import path
from empanadas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empanadas/', views.empanadas, name='liste_empanadas'),
    path('ingredients/', views.ingredients, name='liste_ingredients'),
    path('empanada/<int:empanada_id>/', views.empanada),
    path('ingredients/add', views.formulaireCreationIngredient),
    path('ingredients/create/', views.creerIngredient),
    path('empanadas/add', views.formulaireCreationEmpanada),
    path('empanadas/create/', views.creerEmpanada),
    path('empanada/<int:empanada_id>/addIngredient', views.ajouterIngredientDsEmpanada),
    path('empanada/<int:empanada_id>/delete/', views.supprimerEmpanada),
    path('empanada/<int:empanada_id>/update/', views.afficherFormulaireModificationEmpanada),
    path('empanada/<int:empanada_id>/updated/', views.modifierEmpanada),
    path('ingredients/<int:ingredient_id>/delete/', views.supprimerIngredient),
    path('ingredients/<int:ingredient_id>/update/', views.afficherFormulaireModificationIngredient),
    path('ingredients/<int:ingredient_id>/updated/', views.modifierIngredient),
]
