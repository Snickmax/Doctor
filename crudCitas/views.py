from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from .form import FormularioCitas
from core.models import cita
from django.forms import model_to_dict
from django.template.loader import render_to_string

@login_required(login_url='/login/')
@never_cache
def citas_view(request):
    all_citas = cita.objects.all()
    return render(request, 'citas.html', {'citas': all_citas})

@login_required(login_url='/login/')
@never_cache
def registrar_cita(request):
    if request.method == "POST":
        form = FormularioCitas(request.POST)
        if form.is_valid():
            form.save()

            return JsonResponse({"success": "Cita registrada correctamente. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)
    
@login_required(login_url='/login/')
@never_cache
def actualizar_cita(request, cita_id):
    cita = cita.objects.get(id=cita_id)
    old_cita_data = model_to_dict(cita)  # Guarda los datos antiguos del cita
    if request.method == "POST":
        form = FormularioCitas(request.POST, instance=cita)
        print(form.errors)
        if form.is_valid():
            form.save()
            new_cita_data = model_to_dict(cita)  # Guarda los nuevos datos del cita

            if old_cita_data != new_cita_data:  # Compara los datos antiguos y nuevos
                return JsonResponse({"success": "cita actualizada correctamente. Recargando página..."})

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
        form = FormularioCitas()
        titulo_modal = '<i class="fa-solid fa-patient-plus"></i> Agregar Paciente'
        form_html = render_to_string("citas/registrar.html", {"form": form}, request=request)
    elif form_type == "editar":
        try:
            patient = get_object_or_404(cita, rut=patient_id)
            form = FormularioCitas(instance=patient)
            titulo_modal = '<i class="fa-solid fa-patient-pen"></i> Editar Paciente'
            form_html = render_to_string("citas/editar.html", {"form": form, "patient_id": patient_id}, request=request)
        except cita.DoesNotExist:
            return JsonResponse({"error": "El paciente especificado no existe."}, status=404)
    else:
        return JsonResponse({"error": "Tipo de formulario no válido."}, status=400)

    return JsonResponse({"form_html": form_html, "titulo_modal": titulo_modal})