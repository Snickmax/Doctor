from django.urls import path
from . import Pacientes

urlpatterns = [
    path('dashboardC/', Pacientes.pacientes_view, name='dashboardC'),
    path('dashboardP/', Pacientes.pacientes_view, name='dashboardP'),
    
    path('cargar_formulario/', Pacientes.cargar_formulario, name='cargar_formulario'),
    path('registrar_paciente/', Pacientes.registrar_paciente, name='registrar_paciente'),
    path('actualizar_paciente/<str:patient_id>/', Pacientes.actualizar_paciente, name='actualizar_paciente'),
]