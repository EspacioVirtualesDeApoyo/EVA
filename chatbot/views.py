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
            "buenos dias|buen dia|buenas tardes|buenas noches|hola|hola eva": "¿En qué puedo ayudarte?\nPor favor, indícame en qué puedo ayudarte.",
            
            # Información sobre contactos
            "contactos": '1. Línea Púrpura Bogotá\n• Llamando al 018000112137\n• Escribiendo al WhatsApp 3007551846',
            
            # Violencia de género
            "violencia": (
                "La violencia de género puede adoptar muchas formas, incluyendo violencia física, emocional, psicológica, sexual y económica.\n\n"
                "Es importante saber que la violencia no es tu culpa. Nadie merece vivir en una situación de violencia.\n\n"
                "Si estás sufriendo violencia, puedes comunicarte con la Línea Púrpura llamando al 018000112137 o escribiendo al WhatsApp 3007551846.\n"
                "También puedes buscar apoyo en un psicólogo o acudir a algún refugio seguro si es necesario."
            ),
            
            # Cómo identificar si eres víctima
            "como identificar violencia|señales de violencia|victima de violencia": (
                "Algunas señales de que podrías estar sufriendo violencia de género incluyen:\n\n"
                "1. **Violencia física**: golpes, empujones, quemaduras, lesiones.\n"
                "2. **Violencia emocional y psicológica**: insultos, humillaciones, intimidación, control excesivo sobre tus decisiones.\n"
                "3. **Violencia sexual**: presiones para tener relaciones sexuales sin tu consentimiento o abuso sexual.\n"
                "4. **Violencia económica**: control sobre tu dinero, no dejarte trabajar, no permitirte decidir sobre tus gastos.\n\n"
                "Si alguna de estas situaciones te resulta familiar, puede ser una señal de que necesitas ayuda. No estás sola y hay recursos para ti."
            ),
            
            # Palabras de motivación
            "motivar|palabras de apoyo|estoy sufriendo|me siento triste|me siento sola|me siento mal": (
                "Lamento mucho que estés pasando por esto. Quiero que sepas que eres muy valiente por estar buscando ayuda y que mereces vivir una vida sin violencia. "
                "Recuerda que nadie tiene derecho a controlarte, humillarte o hacerte daño. Hay un futuro mejor para ti, lleno de paz y seguridad. "
                "Si necesitas hablar con alguien, no dudes en contactarme o buscar apoyo profesional. El primer paso hacia la sanación es hablar sobre lo que estás viviendo."
            ),
            
            # Recursos de apoyo
            "recursos de apoyo|ayuda emocional|apoyo psicológico": (
                "Existen muchas formas de obtener ayuda. Además de la Línea Púrpura, puedes buscar un psicólogo o terapeuta especializado en violencia de género. "
                "También puedes asistir a grupos de apoyo o acudir a tu centro de salud más cercano para obtener orientación. "
                "Nunca dudes en buscar ayuda. La violencia de género no debe ser tolerada, y mereces vivir en un ambiente seguro y saludable."
            ),
            
            # Estrategias de protección
            "estrategias de proteccion|como protegerme|siento miedo": (
                "Si estás en una situación donde sientes que estás en peligro, tu seguridad es lo más importante. Algunas estrategias incluyen:\n\n"
                "1. **Tener un plan de emergencia**: Si sientes que hay una amenaza inmediata, trata de tener a mano tu teléfono y el contacto de una persona de confianza a la que puedas avisar.\n"
                "2. **Busca un lugar seguro**: Si es posible, sal de la situación y dirígete a un lugar seguro (casa de un amigo, familiar o refugio).\n"
                "3. **Llamada de emergencia**: Si estás en peligro, no dudes en llamar a la policía o utilizar la Línea Púrpura.\n\n"
                "Es importante que busques apoyo de profesionales que puedan ayudarte a planificar tu seguridad a largo plazo."
            ),
            
            # Apoyo emocional y cómo salir de la situación
            "salir de la violencia|terminar la relación|escapar de la violencia": (
                "Salir de una situación de violencia de género es difícil, pero es posible. El primer paso es reconocer que mereces estar en una relación sana y sin miedo. "
                "Es importante contar con el apoyo de personas de confianza y, si es posible, buscar ayuda profesional para guiarte a través de este proceso. "
                "Recuerda que tienes derecho a una vida sin violencia, y el camino hacia la recuperación es posible. Si te sientes insegura o no sabes cómo dar el siguiente paso, "
                "hay muchos recursos disponibles para guiarte y protegerte."
            ),
            
            # Respuesta cuando se agradece la ayuda
            "gracias": "¡De nada! Si necesitas algo más, no dudes en preguntar.\n• ¡Estoy aquí para ayudarte en cualquier momento!",
            
            # Cierre de conversación
            "fin": "Gracias por hablar conmigo. No olvides que siempre puedes buscar apoyo cuando lo necesites. ¡Cuídate mucho!"
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
