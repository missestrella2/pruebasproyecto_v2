from ventas.models import Venta
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.views import View


def principal(request):
    v=""
    context = {"v": v}
    return render(request, 'login/principal.html', {"context": context})

