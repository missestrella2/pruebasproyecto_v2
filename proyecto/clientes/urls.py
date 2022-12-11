from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns=[
    path('clientes/listadeclientes/', login_required(views.ListaDeClientes.as_view()), name='listadeclientes'),
    path('clientes/altaclienteform', login_required(views.AltaClienteForm.as_view()), name='AltaClienteForm'),
    path('clientes/bajaclienteform', login_required(views.BajaClienteForm.as_view()), name="BajaClienteForm"),
    path('clientes/clienteeditar/<int:id_cliente>', login_required(views.clienteeditar), name='clienteeditar'),
    path('clientes/clienteeliminar/<int:id_cliente>', login_required(views.clienteeliminar), name='clienteeliminar'),
    path('clientes/paginaenblanco/', login_required(views.paginaenblanco), name='paginaenblanco'),
]