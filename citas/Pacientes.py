from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from .form import FormularioPaciente
from core.models import paciente
from django.forms import model_to_dict
from django.template.loader import render_to_string

@login_required(login_url='/login/')
@never_cache
def pacientes_view(request):
    all_patient = paciente.objects.all()
    return render(request, 'pacientes.html', {'pacientes': all_patient})

@login_required(login_url='/login/')
@never_cache
def registrar_paciente(request):
    if request.method == "POST":
        form = FormularioPaciente(request.POST)
        if form.is_valid():
            form.save()

            return JsonResponse({"success": "Paciente registrado correctamente. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)
    
@login_required(login_url='/login/')
@never_cache
def actualizar_paciente(request, patient_id):
    patient = paciente.objects.get(rut=patient_id)
    old_patient_data = model_to_dict(patient)  # Guarda los datos antiguos del Paciente
    if request.method == "POST":
        form = FormularioPaciente(request.POST, instance=patient)
        print(form.errors)
        if form.is_valid():
            form.save()
            new_patient_data = model_to_dict(patient)  # Guarda los nuevos datos del Paciente

            if old_patient_data != new_patient_data:  # Compara los datos antiguos y nuevos
                return JsonResponse({"success": "Paciente actualizado correctamente. Recargando página..."})

            return JsonResponse({"success": "No se realizaron cambios. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)

@login_required(login_url='/login/')
@never_cache
def cargar_formulario(request):
    form_type = request.GET.get("form_type")  # Obtiene el tipo de formulario enviado desde la solicitud AJAX
    patient_id = request.GET.get("patient_id")  # Obtiene el ID del Paciente, si está presente
    
    if form_type == "registro":
        form = FormularioPaciente()
        titulo_modal = '<i class="fa-solid fa-patient-plus"></i> Agregar Paciente'
        form_html = render_to_string("pacientes/registrar.html", {"form": form}, request=request)
    elif form_type == "editar":
        try:
            patient = get_object_or_404(paciente, rut=patient_id)
            form = FormularioPaciente(instance=patient)
            titulo_modal = '<i class="fa-solid fa-patient-pen"></i> Editar Paciente'
            form_html = render_to_string("pacientes/editar.html", {"form": form, "patient_id": patient_id}, request=request)
        except paciente.DoesNotExist:
            return JsonResponse({"error": "El paciente especificado no existe."}, status=404)
    else:
        return JsonResponse({"error": "Tipo de formulario no válido."}, status=400)

    return JsonResponse({"form_html": form_html, "titulo_modal": titulo_modal})