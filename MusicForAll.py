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

    respuesta = requests.get(url, params=parametros)
    datos = respuesta.json()

    biografia = datos["artist"]["bio"]["summary"]   #Este segmento
    if "<a href" in biografia:
        biografia = biografia[:biografia.find("<a href")]

    print(f'Artista:{datos["artist"]["name"]}')
    print(f'Oyentes:{datos["artist"]["stats"]["listeners"]}')
    print(f'biografia:{biografia.strip()}')

buscar_artista("Foo Fighters")
