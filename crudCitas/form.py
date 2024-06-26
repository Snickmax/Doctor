from django import forms
from core.models import cita

class FormularioCitas(forms.ModelForm):
    class Meta:
        model = cita
        fields = ('patient', 'date', 'time', 'reason')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].error_messages = {'unique': 'La hora seleccionada ya está reservada.'}
        