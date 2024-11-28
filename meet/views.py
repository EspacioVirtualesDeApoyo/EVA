# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import EncuentroSincronico
from django.http import JsonResponse
from .models import EncuentroSincronico
from django.views.decorators.http import require_GET
from datetime import timedelta

import calendar


def calendario_home(request):
    return render(request, 'calendario.html')

@require_GET
def fechas_encuentros(request):
    try:
        # Obtener año y mes desde la URL
        año = int(request.GET.get("año", 0))
        mes = int(request.GET.get("mes", 0))

        # Validar parámetros
        if año < 1 or mes < 1 or mes > 12:
            return JsonResponse({"error": "Parámetros inválidos"}, status=400)

        # Filtrar encuentros por fecha
        encuentros = EncuentroSincronico.objects.filter(fecha__year=año, fecha__month=mes)

        # Preparar la respuesta con nombre, fecha (ajustada) y URL
        datos = [
            {
                "nombre": encuentro.nombre,
                "fecha": (encuentro.fecha + timedelta(days=1)).strftime("%Y-%m-%d"),  # Ajustar la fecha
                "url": encuentro.url
            }
            for encuentro in encuentros
        ]

        # Enviar la respuesta en formato JSON
        return JsonResponse({"encuentros": datos})

    except ValueError:
        return JsonResponse({"error": "Formato de parámetros inválido"}, status=400)

