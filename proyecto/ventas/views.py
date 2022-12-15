from datetime import datetime
from django.shortcuts import render, redirect
#from clientes.models import Cliente
#from pagoformas.models import PagoForma
from django.views import View
from django.views.generic import ListView

from ventas.forms import VentasForm, AltaVentaForm,BuscarVentaForm
from ventas.models import Venta

#Departamento



def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'ventas/paginaenblanco.html', {"context": context})

# def estadisticas(request):
#     context = {"hoy": datetime.now}
#     return render(request, 'ventas/estadisticas.html', {"context": context})

def buscarventas(request): #filtro por nombre
    ventas = Venta.objects.all()
    ventas=ventas.filter(fecha_de_venta__range=["1900-09-01", "2022-10-31"])
    context={
     'form': BuscarVentaForm(),
     'ventas':ventas,
    }
    return render(request,'ventas/buscarventas.html',context)

class ListaDeVentas(ListView):
    model = Venta 
    context_object_name = 'ventas'
    template_name = 'ventas/listadeventas.html'
    ordering =['id']

# class ListaDeDptos(ListView):
#     model = Departamento
#     context_object_name = 'departamentos'
#     template_name = 'ventas/listadeventas.html'
#     ordering =['id']


class altaventaform(View): #FORMULARIO DE ALTA
    form_class = AltaVentaForm
    template_name = 'ventas/altaventaform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadeventas')

        return render(request, self.template_name, {'formulario': form})