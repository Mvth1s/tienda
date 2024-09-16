from django.db import models

# Create your models here.

class Ingredient(models.Model):
    #cle primaire, avec auto-incrementation
    idIngredient = models.AutoField(primary_key=True)
    #chaine de caractere de taille bornee
    nomIngredient = models.CharField(max_length=50)
    #version python du toString(), utilisee par django dans ses interfaces
    def __str__(self) :
        return self.nomIngredient
    
class Empanada(models.Model):
    #cle primaire, avec auto-incrementation
    idEmpanada = models.AutoField(primary_key=True)
    #chaine de caractere de taille bornee
    nomEmpanada = models.CharField(max_length=50)
    #nombre decima, max 6 chiffres dont 2 apres la virgule
    prix = models.DecimalField(max_digits=6, decimal_places=2,)
    #version python du toString(), utilisee par django dans ses interfaces
    def __str__(self) :
        return 'empanada '+self.nomEmpanada+' (prix:'+str(self.prix)+'€)'