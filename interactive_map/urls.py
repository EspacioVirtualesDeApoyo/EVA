from django.urls import path
from . import views
from .views import mapa_view

urlpatterns = [
    path("", mapa_view, name="mapa"),
]
