from django.urls import path, include
from rest_framework.routers import DefaultRouter
from proyecto_api import views

router = DefaultRouter()
router.register(r'clientes',views.Cliente,basename='cliente')

urlpatterns =[
    path('',include(router.urls)),
    path('api-auth',include('rest_framework.urls',namespace='rest_framework'))

]


