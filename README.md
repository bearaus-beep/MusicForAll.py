MusicForAll

Descripcion: Herramienta de consola para periodistas y aficionados musicales que permite investigar artistas usando la API de Last.fm, entregando toda la información relevante en un solo lugar.

Stakeholder: Un periodista musical o simplemente un aficionado a la musica que necesita conocer a un artista o a diversos artistas que esten en los tops de las plataformas mas ocupadas.

Problema: Actualmente para conocer a un artista nuevo tiene que investigar en varios sitios webs  o fuentes acerca del artista, lo cual es lento por que es mucha informacion repartida en distintos lugares y no siempre nos dara la informacion que requerimos

Solucion: Esta herramienta permite realizar la busqueda de una manera mucho mas rapida y concisa con un solo input donde ingresaremos el nombre y que reunira la informacion mas relevante del artista. Desde la historia o pequeña bibliografia, sus canciones mas famosas, sus discos mas aclamados y hasta su videoclip mas visto.  Todo en un solo lugar.

Requisitos:
-Docker instalado
-API Key de Last.fm (registro gratiuto en https://www.last.fm/api)

Configuración
Antes de ejecutar, exporta tu API Key como variable de entorno en la terminal:
export LASTFM_API_KEY="tu_clave_aqui"

Como ejecutar con Docker
En la terminal:
    ./build.sh

Ejemplo de salida

Artista: Arctic Monkeys
Oyentes: 7.1M
Géneros: indie rock, indie, british, alternative, rock
Biografia: Arctic Monkeys es una banda de rock alternativo formada en Sheffield, South Yorkshire, Inglaterra en 2002 después de conocerse en Stocksbridge High School. La banda está formada por Alex Turner (voz, guitarra, piano), Jamie Cook (guitarra), Nick O'Malley (coros, bajo) y Matt Helders (batería, voz). El bajista fundador Andy Nicholson se fue en 2006.

Son una de las primeras bandas en llamar la atención del público a través de Internet a través de MySpace, a pesar de que ninguno de ellos tiene una cuenta.

Top Canciones:
1. 505 - 58.5M reproducciones - 3.0M oyentes
2. Do I Wanna Know? - 45.3M reproducciones - 2.9M oyentes
3. Why'd You Only Call Me When You're High? - 41.9M reproducciones - 2.7M oyentes
4. I Wanna Be Yours - 42.6M reproducciones - 2.6M oyentes
5. Fluorescent Adolescent - 34.5M reproducciones - 2.5M oyentes

Top Albums:
1. AM - 265.4M reproducciones
2. Favourite Worst Nightmare - 155.2M reproducciones
3. Whatever People Say I Am, That's What I'm Not - 140.7M reproducciones
4. Favourite Worst Nightmare (Standard Version) - 47.2M reproducciones
5. Humbug - 69.8M reproducciones