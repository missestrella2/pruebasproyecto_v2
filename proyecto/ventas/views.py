from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

from ventas.forms import AltaVentaForm,BuscarVentaForm
from ventas.forms import DepartamentosForm, AltaDepartamentoForm,BajaDepartamentoForm
from ventas.models import Venta,Departamento

from django.core.mail import send_mail
from datetime import timedelta
from datetime import datetime
from datetime import date

def paginaenblanco(request):
    context = {"hoy": datetime.now}
    return render(request, 'ventas/paginaenblanco.html', {"context": context})

#def buscarventas(request): 
########## esta mal encarado, porque usa un intervalo fijo
########## y tiene que ser variable la fecha
#
#   ventas = Venta.objects.all()
#   ventas=ventas.filter(fecha_de_venta__range=["1900-09-01", "2022-10-31"])
    # context={
    #  'form': BuscarVentaForm(),
    #  'ventas':ventas,
    # }
    # return render(request,'ventas/buscarventas.html',context)

def buscarventas(request): #filtro por los que no compran hace mas de tres meses
    ventas = Venta.objects.all()
    #date.today es hoy, timedelta(days=90) es un intervalo de 90 dias
    #hoy menos 90 dias da una fecha, esa fecha se debe convertir en string
    #  lte es para filtre los menores o iguales a  
    ventas = ventas.filter(fecha_de_venta__lte=str(date.today()-timedelta(days=90)))
    ventas= ventas.order_by('-estado_pendiente')
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

class estadisticas(ListView):
    model = Venta 
    context_object_name = 'estadisticas'
    template_name = 'ventas/estadisticas.html'
    ordering =['id']

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

def estadocambiar(request, id): #BOTON CAMBIAR DE ESTADO y mandar mail
    try:
         venta2 = Venta.objects.get(id=id)
    except Venta.DoesNotExist:
         return render(request, 'ventas/404.html')

    if (venta2.estado_pendiente==True):
        send_mail(
                    'TE EXTRAÑAMOS '+venta2.clientes.nombre,
                    'Hola '+venta2.clientes.nombre+', como estas? Hace mucho que no nos vemos. Por eso te ofrecemos esta promo exclusiva para vos: Presentando este mail tenes 20% OFF en todos nuestros productos. Te esperamos!',
                    'pruebasdjango2022gmail.com',
                    [venta2.clientes.email],
                    fail_silently=False) 
        venta2.estado_pendiente=False
        venta2.estado_terminado=True
        venta2.save()
  
    return redirect('buscarventas')



######################DEPARTAMENTOS####################################

class ListaDeDepartamentos(ListView):
    model = Departamento 
    context_object_name = 'departamentos'
    template_name = 'ventas/listadedepartamentos.html'
    ordering =['id']

def departamentoeditar(request, id_departamento): #BOTON EDITAR EN LISTADO
    try:
        departamento = Departamento.objects.get(id=id_departamento)
    except Departamento.DoesNotExist:
        return render(request, 'ventas/404.html')
    
    if request.method == "POST":
        formulario = DepartamentosForm(request.POST, instance=departamento)
        if formulario.is_valid():
            formulario.save()
            return redirect('listadedepartamentos')
    else:
        formulario = DepartamentosForm(instance=departamento)

    return render(request, 'ventas/departamentoeditar.html', {'formulario': formulario, 'id_departamento': id_departamento})


def departamentoeliminar(request, id_departamento): #BOTON ELIMINAR EN LISTADO 
    try:
        departamento = Departamento.objects.get(id=id_departamento)
    except Departamento.DoesNotExist:
        return render(request, 'ventas/404.html')
    departamento.delete()
    return redirect('listadedepartamentos')


class AltaDepartamentoForm(View): #FORMULARIO DE ALTA
    form_class = AltaDepartamentoForm
    template_name = 'ventas/altadepartamentoform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listadedepartamentos')

        return render(request, self.template_name, {'formulario': form})

class BajaDepartamentoForm(View): #FORMULARIO DE BAJA
    form_class = BajaDepartamentoForm
    template_name = 'ventas/bajadepartamentoform.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'formulario': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
      
            try:
                departamento_a_borrar= Departamento.objects.get(nombre=nombre)
            except Departamento.DoesNotExist:
                return render(request, "ventas/404.html")    
           
            departamento_a_borrar.delete()
        else: 
            return redirect('listadedepartamentos')

        return render(request, self.template_name, {'formulario': form})