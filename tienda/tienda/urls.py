from django.contrib import admin
from django.urls import path
from empanadas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('empanadas/', views.empanadas),
    path('ingredients/', views.ingredients),
    path('empanada/<int:empanada_id>', views.empanada),
    path('ingredients/add', views.formulaireCreationIngredient),
    path('ingredients/create/', views.creerIngredient),
    path('empanadas/add', views.formulaireCreationEmpanada),
    path('empanadas/create/', views.creerEmpanada),
]
