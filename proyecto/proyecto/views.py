from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail

from ventas.models import Venta


def index(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        return redirect('login')

def logout_view(request):
     logout(request)
     return redirect('logout')

def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'login/paginaenblanco.html', {"context": context})



