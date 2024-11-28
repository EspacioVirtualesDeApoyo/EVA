# urls.py
from django.urls import path
from . import views
app_name = 'reuniones'
urlpatterns = [
    path('calendarios/', views.calendario_home, name='calendario_home'),
    path('fechas-encuentros/', views.fechas_encuentros, name='fechas_encuentros'),
    path('reuniones/', views.reuniones, name='reuniones'),
]
