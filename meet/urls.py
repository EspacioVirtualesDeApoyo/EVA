# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario_home, name='calendario_home'),
    path('fechas-encuentros/', views.fechas_encuentros, name='fechas_encuentros'),
]
