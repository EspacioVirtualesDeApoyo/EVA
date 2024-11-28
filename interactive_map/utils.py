import folium
import geocoder
import requests

def generate_map():
    # URL de la API de refugios
    api_url = "http://127.0.0.1:8001/refugios"

    # Consumir datos de refugios desde la API
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        refugios = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al consumir la API: {e}")
        refugios = [
            {
                "nombre": "Refugio Seguro La Esperanza",
                "descripcion": "Un refugio de emergencia para mujeres que sufren violencia doméstica.",
                "correo_contacto": "contacto@refugioesperanza.com",
                "direccion": "Calle Ficticia 123, Ciudad Segura",
                "telefono": "+1234567890",
                "whatsapp": "+1234567890",
                "pagina_web": "https://www.refugioesperanza.com",
                "latitud": 4.592420239278098,
                "longitud": -74.12410912022571,
                "imagenes": [],
                "estado": True,
                "tipo": "REFUGIO"
            },
            {
                "nombre": "Parque Central",
                "descripcion": "Un lugar para disfrutar con la familia.",
                "correo_contacto": "info@parquecentral.com",
                "direccion": "Avenida Principal 45, Ciudad Verde",
                "telefono": "+1234567891",
                "whatsapp": "+1234567891",
                "pagina_web": "https://www.parquecentral.com",
                "latitud": 4.590074850197806,
                "longitud": -74.19942825591379,
                "imagenes": [],
                "estado": True,
                "tipo": "LUGAR"
            }
        ]

    # Obtener la ubicación del usuario
    mi_ubicacion = geocoder.ip('me').latlng

    # Crear el mapa centrado en la ubicación del usuario
    mapa = folium.Map(location=mi_ubicacion, zoom_start=13)

    # Agregar marcador para la ubicación del usuario
    folium.Marker(
        location=mi_ubicacion,
        popup="Tú estás aquí",
        icon=folium.Icon(color="blue", icon="female", prefix="fa")  # Icono de mujer para la ubicación del usuario
    ).add_to(mapa)

    # Agregar marcadores para refugios y lugares
    for refugio in refugios:
        icono = None

        # Cambiar icono basado en el tipo
        if refugio["tipo"] == "REFUGIO":
            icono = folium.Icon(color="purple", icon="home", prefix="fa")  # Casita con corazón
        elif refugio["tipo"] == "LUGAR":
            icono = folium.Icon(color="orange", icon="plus-square", prefix="fa")  # Casita con cruz

        # Crear el popup con detalles
        popup_content = f"""
            <div style="width: 200px;">
                <h4>{refugio["nombre"]}</h4>
                <p>{refugio["descripcion"]}</p>
                <p><b>Dirección:</b> {refugio["direccion"]}</p>
                <p><b>Teléfono:</b> {refugio["telefono"]}</p>
                <p><b>Correo:</b> <a href="mailto:{refugio['correo_contacto']}">{refugio['correo_contacto']}</a></p>
                <p><b>WhatsApp:</b> {refugio["whatsapp"]}</p>
                <p><b>Página web:</b> <a href="{refugio['pagina_web']}" target="_blank">{refugio['pagina_web']}</a></p>
            </div>
        """

        # Agregar marcador con icono personalizado
        folium.Marker(
            location=[refugio["latitud"], refugio["longitud"]],
            popup=folium.Popup(popup_content, max_width=300),
            icon=icono
        ).add_to(mapa)

    # Devolver el mapa renderizado en formato HTML
    return mapa._repr_html_()
