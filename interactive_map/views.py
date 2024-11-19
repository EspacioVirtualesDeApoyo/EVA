from django.shortcuts import render
from .utils import generate_map

def mapa_view(request):
    mapa_html = generate_map()
    return render(request, "maps/interactive_map.html", {"map": mapa_html})
