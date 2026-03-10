from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render <-- esta libreria no la usamos por ahora
from rest_framework import viewsets
from .serializer import ProgrammerSerializer
from .models import programmer
# Create your views here.

from rest_framework.permissions import IsAuthenticated


class ProgrammerViewSet(viewsets.ModelViewSet):
    # acá creamos una consulta o QUERY a nuestra tabla, trayendo todos los campos como un objeto.
    queryset = programmer.objects.all()
    # Agregamos la clase ProgrammerSerializer que ya tiene el modelo serializado para mostrar
    serializer_class = ProgrammerSerializer
    # permission_classes = [IsAuthenticated]
    # esta línea es para que solo usuarios autenticados puedan ver la API - JWT


def home(request):
    return render(request, "home.html")
