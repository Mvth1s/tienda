from django.urls import path
from django.contrib.auth import views as auth_views
from comptes import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'comptes/login.html'), name = 'login'),
    path('logout/', views.deconnexion, name='logout'),
    path('connexion/', views.connexion),
    path('user/update/', views.formulaireProfil),
    path('user/updated/', views.traitementFormulaireProfil),
    path('register/', views.formulaireInscription),
    path('inscription/', views.traitementFormulaireInscription),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name = 'comptes/password_reset.html',
        email_template_name = 'comptes/password_reset_email.html'),
        name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name = 'comptes/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name = 'comptes/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name = 'comptes/password_reset_complete.html'),
        name='password_reset_complete'),
]