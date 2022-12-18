from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns=[
    path('ventas/altaventaform', login_required(views.altaventaform.as_view()), name='altaventaform'),
   # path('ventas/bajaventaform', login_required(views.bajaventaform.as_view()), name="bajaventaform"),
   # path('ventas/ventaeditar/<int:id_venta>', login_required(views.ventaeditar), name='ventaeditar'),
   # path('ventas/ventaeliminar/<int:id_venta>', login_required(views.ventaeliminar), name='ventaeliminar'),
    path('ventas/paginaenblanco/', login_required(views.paginaenblanco), name='paginaenblanco'),
    path('ventas/listadedeventas/', login_required(views.ListaDeVentas.as_view()), name='listadeventas'),

    path('ventas/buscarventas/', login_required(views.buscarventas), name='buscarventas'),
    path('ventas/estadocambiar/<int:id>', login_required(views.estadocambiar), name='estadocambiar'),

    path('ventas/listadedepartamentos/', login_required(views.ListaDeDepartamentos.as_view()), name='listadedepartamentos'),
    path('ventas/altadepartamentoform', login_required(views.AltaDepartamentoForm.as_view()), name='altadepartamentoform'),
    #path('ventas/bajadepartamentoform', login_required(views.BajaDepartamentoForm.as_view()), name="bajadepartamentoform"),
    path('ventas/departamentoeditar/<int:id_departamento>', login_required(views.departamentoeditar), name='departamentoeditar'),
    path('ventas/departamentoeliminar/<int:id_departamento>', login_required(views.departamentoeliminar), name='departamentoeliminar'),

    path('ventas/estadisticas/', login_required(views.estadisticas.as_view()), name='estadisticas'),


]