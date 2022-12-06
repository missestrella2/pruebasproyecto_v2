from datetime import datetime
from multiprocessing import context
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from clientes.forms import ClientesForm, AltaClienteForm, BajaClienteForm
from django.contrib import messages
from ventas.models import Cliente
from django.views import View
from django.views.generic import ListView


def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'clientes/paginaenblanco.html', {"context": context})

class ListaDeClientes(ListView):
    model = Cliente 
    context_object_name = 'clientes'
    template_name = 'clientes/listadeclientes.html'
    ordering =['id']

def clienteeditar(request, id_cliente): #BOTON EDITAR EN LISTADO
    try:
        cliente = Cliente.objects.get(id=id_cliente)
    except Cliente.DoesNotExist:
        return render(request, 'clientes/404.html')
    
    if request.method == "POST":
        formulario = ClientesForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect('listadeclientes')
    else:
        formulario = ClientesForm(instance=cliente)

    return render(request, 'clientes/clienteseditar.html', {'formulario': formulario, 'id_cliente': id_cliente})


def clienteeliminar(request, id_cliente): #BOTON ELIMINAR EN LISTADO 
    try:
        cliente = Cliente.objects.get(id=id_cliente)
    except Cliente.DoesNotExist:
        return render(request, 'clientes/404.html')
    cliente.delete()
    return redirect('listadeclientes')


class AltaClienteForm(View): #FORMULARIO DE ALTA
    form_class = AltaClienteForm
    template_name = 'prueba_clientes/altaclienteform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadeclientes')

        return render(request, self.template_name, {'formulario': form})

class BajaClienteForm(View): #FORMULARIO DE BAJA
    form_class = BajaClienteForm
    template_name = 'prueba_clientes/bajaclienteform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
      
            try:
                cliente_a_borrar= Cliente.objects.get(nombre=nombre,apellido=apellido,email=email)
            except Cliente.DoesNotExist:
                return render(request, "prueba_clientes/404.html")    
           
            cliente_a_borrar.delete()
        else: 
            return redirect('listadeclientes')

        return render(request, self.template_name, {'formulario': form})