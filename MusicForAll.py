import requests
import os

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
            print(f'Artista: {datos["artist"]["name"]}')
            print(f'Oyentes: {datos["artist"]["stats"]["listeners"]}')
            print(f'Biografia: {biografia.strip()}')

    except requests.exceptions.ConnectionError:
        print("Error: no hay conexión a internet")
    except requests.exceptions.Timeout:
        print("Error: la API tardó demasiado")

buscar_artista("Foo Fighters")