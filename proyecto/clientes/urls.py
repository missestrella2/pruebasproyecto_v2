from django.urls import path, re_path
from . import views

urlpatterns=[

    path('clientes/listadeclientes/',views.ListaDeClientes.as_view(),name='listadeclientes'),
    path('clientes/altaclienteform', views.AltaClienteForm.as_view(), name='AltaClienteForm'),
    path('clientes/bajaclienteform',views.BajaClienteForm.as_view(),name="BajaClienteForm"),
    path('clientes/clienteeditar/<int:id_cliente>',views.clienteeditar,name='clienteeditar'),
    path('clientes/clienteeliminar/<int:id_cliente>',views.clienteeliminar,name='clienteeliminar'),
    path('clientes/paginaenblanco/',views.paginaenblanco,name='paginaenblanco'),
]