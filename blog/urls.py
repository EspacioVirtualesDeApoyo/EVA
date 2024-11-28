# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('', views.educacion, name='educacion'),
    path('', views.contacto, name='contacto'),
]
