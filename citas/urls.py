from django.urls import path
from . import views

urlpatterns = [
    path('dashboardC/', views.usuarios_view, name='dashboardC'),
    path('cargar_formulario/', views.cargar_formulario, name='cargar_formulario'),
    
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('actualizar_usuario/<int:user_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('actualizar_pass/<int:user_id>/', views.actualizar_pass, name='actualizar_pass'),
]