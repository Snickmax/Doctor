from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import usuarios
from django.utils.translation import gettext_lazy as _

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = usuarios
        fields = ('username', 'first_name', 'last_name', 'last_name2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': 'El nombre de usuario ya está en uso.'}
        self.fields['email'].error_messages = {'unique': 'El correo ya está en uso.'}

class FormularioEditar(UserChangeForm):
    is_active = forms.ChoiceField(choices=[(1, 'Activo'), (0, 'Inactivo')])
    class Meta:
        model = usuarios
        fields = ('username', 'first_name', 'last_name', 'last_name2', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': 'El nombre de usuario ya está en uso.'}
        self.fields['email'].error_messages = {'unique': 'El correo ya está en uso.'}