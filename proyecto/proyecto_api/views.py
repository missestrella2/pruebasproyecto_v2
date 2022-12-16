from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions
from clientes.models import Cliente
from proyecto_api import serializers

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
