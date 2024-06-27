from django import forms
from core.models import cita

class FormularioCitas(forms.ModelForm):
    class Meta:
        model = cita
        fields = ('patient', 'date', 'time', 'reason')
        
    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # Verifica si ya existe una cita para el paciente en la misma fecha y hora
        if date and time:
            existing_cita = cita.objects.filter(date=date, time=time).exists()
            if existing_cita:
                self.add_error('time', 'La hora seleccionada ya está reservada.')

        return cleaned_data
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].error_messages = {'unique': 'La hora seleccionada ya está reservada.'}
        self.fields['time'].error_messages = {'unique': 'La hora seleccionada ya está reservada.'}
        