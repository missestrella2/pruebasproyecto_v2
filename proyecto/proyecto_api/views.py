
from rest_framework import viewsets
from rest_framework import permissions
from clientes.models import Cliente
from proyecto_api import serializers


# Create your views here.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('id')
    serializer_class = serializers.ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]