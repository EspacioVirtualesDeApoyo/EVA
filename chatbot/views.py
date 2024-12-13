from django.shortcuts import render
from django.http import JsonResponse
import unicodedata

def normalizar_texto(texto):
    # Elimina tildes y normaliza a caracteres básicos
    texto_normalizado = unicodedata.normalize('NFD', texto)
    texto_sin_tildes = ''.join(char for char in texto_normalizado if unicodedata.category(char) != 'Mn')
    return texto_sin_tildes.lower()

def chatbot_interface(request):
    return render(request, 'chatbot/chat_interface.html')

def chatbot_response(request):
    if request.method == "POST":
        user_message = request.POST.get("message", "")

        # Normaliza el mensaje del usuario
        mensaje_normalizado = normalizar_texto(user_message)

        # Lógica para respuestas predeterminadas con varias palabras clave para un solo resultado
        responses = {
            # Saludos
            "buenos dias|buen dia|buenas tardes|buenas noches|hola|hola eva": (
                "Hola! En que puedo ayudarte hoy? "
            ),

            # Información sobre contactos
            "contactos|contacto": (
                "1. **Línea Púrpura Bogotá**\n"
                "   • Teléfono: 018000112137\n"
                "   • WhatsApp: 3007551846\n\n"
                "2. **Línea 155**\n"
                "   Disponible a nivel nacional, brinda orientación y apoyo a mujeres víctimas de violencia de género.\n\n"
                "3. **Línea 123**\n"
                "   Atención inmediata por la Policía Nacional."
            ),

            # Derechos de las mujeres
            "derechos de las mujeres": (
                'En Colombia, las mujeres tienen derecho a vivir una vida libre de violencia, a la igualdad y no discriminación,'
                'conforme a lo estipulado en la Ley 1257 de 2008. Esta ley establece medidas de prevención, protección y sanción frente a la violencia de género.'
            ),

            # Violencia de género
            "violencia|tipos de violencia": (
                "La violencia de género puede manifestarse de varias formas, incluyendo:\n\n"
                "1. **Violencia física**: golpes, empujones o lesiones.\n"
                "2. **Violencia psicológica**: humillaciones, control excesivo o manipulación emocional.\n"
                "3. **Violencia económica**: privación de recursos o control sobre tus ingresos.\n"
                "4. **Violencia sexual**: actos sin tu consentimiento.\n\n"
                "Recuerda que la Ley 1257 de 2008 te protege y que puedes buscar ayuda en las líneas de atención disponibles."
            ),

            # Guía para realizar una denuncia
            "denunciar|denuncias|denuncia|demanda|demandas": (
                "Si deseas realizar una denuncia por violencia de género, puedes acudir a:\n\n"
                "1. **Fiscalía General de la Nación**: Presenta tu denuncia en cualquier URI o seccional.\n"
                "2. **Comisarías de Familia**: Brindan protección inmediata y medidas de atención.\n"
                "3. **Línea 155**: Recibirás orientación sobre cómo proceder.\n\n"
                "Es importante presentar cualquier evidencia disponible, como mensajes, fotos o testimonios."
            ),

            # Cómo identificar si eres víctima
            "como identificar violencia|señales de violencia|victima de violencia": (
                "Algunas señales de violencia incluyen:\n\n"
                "- **Control excesivo**: Tu pareja limita tus decisiones o contactos.\n"
                "- **Aislamiento**: Te aleja de tu familia o amigos.\n"
                "- **Amenazas**: Te intimida con palabras o gestos.\n\n"
                "Si identificas alguna de estas señales, busca apoyo. Puedes llamar a la Línea Púrpura o acudir a una comisaría de familia."
            ),

            # Palabras de motivación
            "motivar|palabras de apoyo|estoy sufriendo|me siento triste|me siento sola|me siento mal": (
                "Siento mucho lo que estás viviendo. Recuerda que eres fuerte y mereces vivir en un entorno seguro. \n"
                "Buscar ayuda es un acto valiente. Puedes contar con los recursos disponibles en Colombia, como la Línea Púrpura o la Línea 155."
            ),

            # Recursos de apoyo
            "recursos de apoyo|ayuda emocional|apoyo psicológico": (
                "Existen múltiples recursos en Colombia para apoyarte:\n\n"
                "1. **Línea Púrpura**: Orientación especializada para mujeres víctimas de violencia.\n"
                "2. **Grupos de apoyo**: Busca en tu comunidad o instituciones como las Casas de la Mujer.\n"
                "3. **Atención en salud**: Acude a tu EPS o centro de salud más cercano para obtener ayuda psicológica."
            ),

            # Estrategias de protección
            "estrategias de proteccion|como protegerme|siento miedo": (
                "Si estás en peligro, toma medidas para protegerte:\n\n"
                "1. **Plan de emergencia**: Identifica un lugar seguro y contactos de confianza.\n"
                "2. **Documentación**: Mantén tus documentos y objetos esenciales a mano.\n"
                "3. **Llamadas de emergencia**: Marca la Línea 123 o busca apoyo en una comisaría de familia.\n\n"
                "Tu seguridad es prioritaria."
            ),

            # Apoyo emocional y cómo salir de la situación
            "salir de la violencia|terminar la relación|escapar de la violencia": (
                "Salir de una situación de violencia es un proceso difícil pero posible.\n"
                "1. **Busca apoyo**: Habla con alguien de confianza.\n"
                "2. **Contacta profesionales**: Acude a comisarías de familia o terapeutas especializados.\n"
                "3. **Crea un plan de acción**: Define cómo garantizar tu seguridad y bienestar."
            ),

            # Respuesta cuando se agradece la ayuda
            "gracias": (
                "¡De nada! Estoy aquí para ayudarte. Si necesitas más información o apoyo, no dudes en preguntar."
            )
        }

        # Recorre todas las claves y devuelve la respuesta correspondiente
        for clave, respuesta in responses.items():
            # Comprobamos si alguna de las palabras clave (separadas por "|") está en el mensaje
            claves = clave.split('|')
            for palabra_clave in claves:
                if palabra_clave in mensaje_normalizado:
                    return JsonResponse({"response": respuesta})
                

        # Respuesta por defecto si no se encuentra ninguna palabra clave
        return JsonResponse({"response": "Lo siento, no te entiendo. ¿Puedes repetir tu pregunta?"})

    return JsonResponse({"error": "Método no permitido"}, status=405)
