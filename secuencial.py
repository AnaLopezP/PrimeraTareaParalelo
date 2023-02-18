import random
from time import sleep

urls = ['a.com', 'b.com', 'c.com', 'd.com'] #Lista con las supuestas urls

#Funcion que da un tiempo de duración aleatorio por url
def links(url):
    print('Empezando', url)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print('Termiunado', url, 'Tiempo', duracion, 's')
    return url, duracion

#Añadimos las urls con su duracion de procesamiento en una lista
salida = []
for url in urls:
    resultado = links(url)
    salida.append(resultado)

    