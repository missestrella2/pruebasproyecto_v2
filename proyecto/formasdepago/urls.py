from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns=[

    path('pagoformas/listadepagoformas/', login_required(views.ListaDePagoFormas.as_view()), name='listadepagoformas'),
    path('pagoformas/altapagoformaform/', login_required(views.altapagoformaform.as_view()), name='altapagoformaform'),
    path('pagoformas/bajapagoformaform/', login_required(views.bajapagoformaform.as_view()), name="bajapagoformaform"),
    path('pagoformas/pagoformaeditar/<int:id_pagoforma>', login_required(views.pagoformaeditar), name='pagoformaeditar'),
    path('pagoformas/pagoformaeliminar/<int:id_pagoforma>', login_required(views.pagoformaeliminar), name='pagoformaeliminar'),
    path('pagoformas/paginaenblanco/', login_required(views.paginaenblanco), name='paginaenblanco'),
]