from multiprocessing import Pool
import random
from time import sleep

urls =  ['a.com', 'b.com', 'c.com', 'd.com', 'e.com'] #Lista con las supuestas urls, añadimos una nueva url

#Funcion que da un tiempo de duracion aleatorio por url (reciclado)
def links(url):
    print('Empezando', url)
    duracion = round(random.random(), 3)
    sleep(duracion)
    print('Termiunado', url, 'Tiempo', duracion, 's')
    return url, duracion

if __name__ == '__main__':
    piscina = Pool(processes = 4)
    datos = piscina.map(links, urls)

    piscina.close()
    print()

    for row in datos:
        print(row)