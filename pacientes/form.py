from django import forms
from core.models import paciente

class FormularioPaciente(forms.ModelForm):
    class Meta:
        model = paciente
        fields = ('rut', 'first_name', 'last_name', 'last_name2', 'gender','email', 'date_of_birth', 'phone_number', 'address', 'city', 'state')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rut'].error_messages = {'unique': 'El rut de usuario ya está en uso.'}
        self.fields['email'].error_messages = {'unique': 'El correo ya está en uso.'}

class FormularioEditar(forms.ModelForm):
    is_active = forms.ChoiceField(choices=[(1, 'Activo'), (0, 'Inactivo')])
    
    class Meta:
        model = paciente
        fields = ('rut', 'first_name', 'last_name', 'last_name2', 'gender','email', 'date_of_birth', 'phone_number', 'address', 'city', 'state')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rut'].error_messages = {'unique': 'El rut de usuario ya está en uso.'}
        self.fields['email'].error_messages = {'unique': 'El correo ya está en uso.'}