from django.urls import path
from . import views
from .views import mapa_view

urlpatterns = [
    path("map/", mapa_view, name="map"),
]
