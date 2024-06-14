from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('dashboardC')
        
    if request.method == 'GET':
        return render(request, 'login.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return JsonResponse({"errors": "El nombre de usuario o la contraseña son incorrectos."}, status=400)
        else:
            auth_login(request, user)
            return JsonResponse({"success": ""})

@login_required(login_url='/login/')
@never_cache
def logout(request):
    auth_logout(request)
    return redirect('login')