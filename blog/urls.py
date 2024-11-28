# urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('educacion/', views.educacion, name='educacion'),
    path('contacto/', views.contacto, name='contacto'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('sobre_la_app/', views.sobre_la_app, name='sobre_la_app'),
    path('preguntas_frecuentes/', views.preguntas_frecuentes, name='preguntas_frecuentes'),
    path('testimonios/', views.testimonios, name='testimonios'),

]
