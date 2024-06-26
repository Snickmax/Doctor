from django.urls import path
from . import views

urlpatterns = [
    path('dashboardC/', views.citas_view, name='dashboardC'),
    
    path('cargar_formularioC/', views.cargar_formulario, name='cargar_formularioC'),
    path('registrar_citas/', views.registrar_cita, name='registrar_citas'),
    path('actualizar_citas/<str:patient_id>/', views.actualizar_cita, name='actualizar_citas'),
]