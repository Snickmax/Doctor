from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import JsonResponse
from .form import FormularioEditar, FormularioRegistro
from core.models import usuarios
from django.forms import model_to_dict
from django.contrib.auth.forms import SetPasswordForm
from django.template.loader import render_to_string

@login_required(login_url='/login/')
@never_cache
def usuarios_view(request):
    all_users = usuarios.objects.all()
    return render(request, 'usuarios.html', {'usuarios': all_users})

@login_required(login_url='/login/')
@never_cache
def actualizar_usuario(request, user_id):
    user = usuarios.objects.get(id=user_id)
    old_user_data = model_to_dict(user)  # Guarda los datos antiguos del usuario
    if request.method == "POST":
        form = FormularioEditar(request.POST, instance=user)
        if form.is_valid():
            form.save()
            new_user_data = model_to_dict(user)  # Guarda los nuevos datos del usuario

            if old_user_data != new_user_data:  # Compara los datos antiguos y nuevos
                return JsonResponse({"success": "Usuario actualizado correctamente. Recargando página..."})

            return JsonResponse({"success": "No se realizaron cambios. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)
    
@login_required(login_url='/login/')
@never_cache
def registrar_usuario(request):
    if request.method == "POST":
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()

            return JsonResponse({"success": "Usuario registrado correctamente. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)

@login_required(login_url='/login/')
@never_cache
def actualizar_pass(request, user_id):
    user = usuarios.objects.get(id=user_id)
    if request.method == "POST":
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": "Contraseña actualizada correctamente. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)

@login_required(login_url='/login/')
@never_cache
def cargar_formulario(request):
    form_type = request.GET.get("form_type")  # Obtiene el tipo de formulario enviado desde la solicitud AJAX
    user_id = request.GET.get("user_id")  # Obtiene el ID del usuario, si está presente

    if form_type == "registro":
        form = FormularioRegistro()
        titulo_modal = '<i class="fa-solid fa-user-plus"></i> Agregar Usuario'
        form_html = render_to_string("registrar.html", {"form": form}, request=request)
    elif form_type == "editar":
        user = usuarios.objects.get(id=user_id)
        form = FormularioEditar(instance=user)
        titulo_modal = '<i class="fa-solid fa-user-pen"></i> Editar Usuario'
        form_html = render_to_string("editar.html", {"form": form, "user_id": user_id}, request=request)
    elif form_type == "pass":
        user = usuarios.objects.get(id=user_id)
        form = SetPasswordForm(user)
        titulo_modal = '<i class="fa-solid fa-key"></i> Cambiar Contraseña'
        form_html = render_to_string("pass.html", {"form": form}, request=request)
    else:
        return JsonResponse({"error": "Tipo de formulario no válido."}, status=400)

    return JsonResponse({"form_html": form_html, "titulo_modal": titulo_modal})

@login_required(login_url='/login/')
@never_cache
def actualizar_usuario(request, user_id):
    user = usuarios.objects.get(id=user_id)
    old_user_data = model_to_dict(user)  # Guarda los datos antiguos del usuario
    if request.method == "POST":
        form = FormularioEditar(request.POST, instance=user)
        print(form)
        if form.is_valid():
            form.save()
            new_user_data = model_to_dict(user)  # Guarda los nuevos datos del usuario

            if old_user_data != new_user_data:  # Compara los datos antiguos y nuevos
                return JsonResponse({"success": "Usuario actualizado correctamente. Recargando página..."})

            return JsonResponse({"success": "No se realizaron cambios. Recargando página..."})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        return JsonResponse({"error": "Método no permitido."}, status=405)