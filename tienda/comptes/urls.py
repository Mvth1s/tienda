from django.urls import path
from django.contrib.auth import views as auth_views
from comptes import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'comptes/login.html'), name = 'login'),
    path('logout/', views.deconnexion, name='logout'),
    path('connexion/', views.connexion),
]