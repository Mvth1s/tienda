from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from empanadas import views

urlpatterns = [
    path('empanadas/', views.empanadas, name='liste_empanadas'),
    path('ingredients/', views.ingredients, name='liste_ingredients'),
    path('empanada/<int:empanada_id>/', views.empanada, name='detail_empanada'),
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
    path('empanada/<int:empanada_id>/deleteIngredient/<int:ligne_id>/', views.supprimerIngredientDansEmpanada),
    path('empanada/<int:empanada_id>/updateIngredient/<int:ligne_id>/', views.modifierIngredientDansEmpanada),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)