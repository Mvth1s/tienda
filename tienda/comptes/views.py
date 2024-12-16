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