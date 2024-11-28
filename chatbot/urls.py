from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chatbot_interface, name='chatbot_interface'),
    path('get-response/', views.chatbot_response, name='chatbot_response'),
]
