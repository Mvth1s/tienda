from django.forms import ModelForm
from comptes.models import TiendaUser

class TiendaUserForm(ModelForm):
    class Meta:
        model = TiendaUser
        fields = ['username','first_name', 'last_name', 'email', 'image']