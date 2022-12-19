from django.urls import path, include
from rest_framework.routers import DefaultRouter
from proyecto_api import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet, basename='cliente')

urlpatterns = [
  #  path('proyecto_api/', include(router.urls)),
  #  path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
