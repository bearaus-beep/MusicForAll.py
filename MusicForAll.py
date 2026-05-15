import requests
import os
from deep_translator import GoogleTranslator

def traducir(texto):
    try:
        return GoogleTranslator(source="en", target="es").translate(texto)
    except:
        return texto

def formatear_numero(n):
    try:
        num = int(n)
        if num >= 1_000_000:
            return f"{num/1_000_000:.1f}M"
        elif num >= 1_000:
            return f"{num/1_000:.1f}K"
        return str(num)
    except:
        return n

def obtener_top_canciones(nombre):
    url = "https://ws.audioscrobbler.com/2.0/"
    parametros = {
        "method": "artist.gettoptracks",
        "artist": nombre,
        "api_key": os.getenv("LASTFM_API_KEY"),
        "format": "json",
        "limit": 5
    }
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        datos = respuesta.json()
        return datos["toptracks"]["track"]
    except:
        return []

def obtener_top_albums(nombre):
    url = "https://ws.audioscrobbler.com/2.0/"
    parametros = {
        "method": "artist.gettopalbums",
        "artist": nombre,
        "api_key": os.getenv("LASTFM_API_KEY"),
        "format": "json",
        "limit": 5
    }
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        datos = respuesta.json()
        return datos["topalbums"]["album"]
    except:
        return []

def buscar_artista(nombre):
    url = "https://ws.audioscrobbler.com/2.0/"
    parametros = {
        "method": "artist.getinfo",
        "artist": nombre,
        "api_key": os.getenv("LASTFM_API_KEY"),
        "format": "json"
    }
    try:
        respuesta = requests.get(url, params=parametros, timeout=10)
        datos = respuesta.json()

        if "error" in datos:
            codigo_error = datos["error"]
            if codigo_error == 6:
                print("Error: artista no encontrado, verifica el nombre")
            elif codigo_error == 10:
                print("Error: API key inválida")
        else:
            biografia = datos["artist"]["bio"]["summary"]
            if "<a href" in biografia:
                biografia = biografia[:biografia.find("<a href")]
            biografia = biografia.strip()
            if len(biografia) < 50:
                biografia = "Biografía no disponible para este artista."

            tags = datos["artist"]["tags"]["tag"]
            nombres_tags = [tag["name"] for tag in tags]

            print(f'\nArtista: {datos["artist"]["name"]}')
            print(f'Oyentes: {formatear_numero(datos["artist"]["stats"]["listeners"])}')
            print(f'Géneros: {", ".join(nombres_tags)}')
            print(f'Biografia: {traducir(biografia)}')

            print("\nTop Canciones:")
            canciones = obtener_top_canciones(nombre)
            for i, cancion in enumerate(canciones, 1):
                print(f"{i}. {cancion['name']} - {formatear_numero(cancion['playcount'])} reproducciones - {formatear_numero(cancion['listeners'])} oyentes")

            print("\nTop Albums:")
            albums = obtener_top_albums(nombre)
            for i, album in enumerate(albums, 1):
                print(f"{i}. {album['name']} - {formatear_numero(album['playcount'])} reproducciones")

    except requests.exceptions.ConnectionError:
        print("Error: no hay conexión a internet")
    except requests.exceptions.Timeout:
        print("Error: la API tardó demasiado")

buscar_artista("Arctic Monkeys")