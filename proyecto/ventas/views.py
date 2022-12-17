from datetime import datetime
from django.shortcuts import render, redirect
#from clientes.models import Cliente
#from pagoformas.models import PagoForma
from django.views import View
from django.views.generic import ListView

from ventas.forms import VentasForm, AltaVentaForm,BuscarVentaForm
from ventas.forms import DepartamentosForm, AltaDepartamentoForm,BajaDepartamentoForm
from ventas.models import Venta,Departamento

from django.shortcuts import get_object_or_404 #### https://stackoverflow.com/questions/70856274/django-set-boolean-to-false-when-clicking-a-button
#Departamento

from django.core.mail import send_mail



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

def estadocambiar(request, id): #BOTON CAMBIAR DE ESTADO
     try:
         venta2 = Venta.objects.get(id=id)
     except Venta.DoesNotExist:
         return render(request, 'ventas/404.html')
     venta2.estado_pendiente=False
     venta2.estado_terminado=True
     venta2.save()
        
     send_mail(
                'TE EXTRAÑAMOS '+venta2.clientes.nombre,
                'Hola '+venta2.clientes.nombre+', como estas? Hace mucho que no nos vemos. Por eso te ofrecemos esta promo exclusiva para vos: Presentando este mail tenes 20% OFF en todos nuestros productos. Te esperamos!',
                'pruebasdjango2022gmail.com',
                [venta2.clientes.email],
                fail_silently=False) 
     
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