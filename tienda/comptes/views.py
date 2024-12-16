from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import TiendaUser
from .forms import TiendaUserForm

# Create your views here.

def connexion(request):
    usr = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=usr, password=pwd)
    if user is None:
        return redirect('/login')
    else :
        login(request, user)
        return redirect('/empanadas')
    
def deconnexion(request):
    logout(request)
    return render (request, 'comptes/logout.html')

def formulaireProfil(request):
    user = None
    if request.user.is_authenticated:
        return render(request, 'comptes/profil.html',
        {
            'user':TiendaUser.objects.get(id=request.user.id),
        }
    )
    else:
        return redirect('/login')
    
def traitementFormulaireProfil(request):
    user = None
    if request.user.is_authenticated:
        user = TiendaUser.objects.get(id=request.user.id)
        form = TiendaUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/empanadas')
        else:
            return redirect('/login')
        
def formulaireInscription(request):
        form = TiendaUserForm()
        return render(request,
                    'comptes/formulaireInscription.html',
                    {
                        'form': form}
                    
                    )

def traitementFormulaireInscription(request):
    user = TiendaUser()
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.set_password(request.POST['password'])
    user.image = request.FILES['image']
    user.save()
    login(request, user)
    return redirect('/empanadas')