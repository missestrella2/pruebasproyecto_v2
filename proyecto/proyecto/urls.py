from django.contrib import admin
from django.urls import path
from django.urls import include 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('', include('ventas.urls')),
    path('', include('formasdepago.urls')),
    path('', include('clientes.urls')),

    path('',views.index,name='index'), 
    
    path('accounts/',include('django.contrib.auth.urls')),
    path('paginaenblanco/',views.paginaenblanco,name="paginaenblanco"),
    path('accounts/login/',views.login, name='login'),
    path('adios/',auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    

    path('api-auth/',include('rest_framework.urls')), 
    
]
