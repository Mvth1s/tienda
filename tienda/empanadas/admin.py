from django.contrib import admin
from empanadas.models import Ingredient
from empanadas.models import Empanada
from empanadas.models import Composition
# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Empanada)
admin.site.register(Composition)