from copy import deepcopy
from os import system, name 
import random
from time import sleep 
import time

def clear():  
    #if name == 'nt': 
    #    _ = system('cls')
    pass 

def creaLaberinto(formaLaberinto) :
    """ Crea un laberinto a partir de una tira de entrada.
        Entradas:
             formaLaberinto : tira que contiene el diseño del
                         laberinto.
        Salidas:
             Laberinto representado por una matriz, tal que
             la entrada i,j contiene: 0 - si la casilla está
             libre, 1 - si hay pared, 3 - posición en donde
             está la salida.
    """
 
    lista = formaLaberinto.split()
    lista = [ x[:-1] if x[-1] == "\n" else x for x in lista]
    lista = [[int(ch) for ch in x] for x in lista]
    return lista
 
def impLab(laberinto):
    """ Imprime un laberinto.
        Entradas:
             laberinto : laberinto a imprimir.
     """
         
    for x in laberinto:
        for y in x:
            print(y, end= "")
        print()
 

def recorrido(i, j, laberinto):
    """ Dado un laberinto en donde se ubica uno o mas quesos/salidas,
        retorna en una lista de pares ordenados (x,y)
        que indican el camino mas corto desde una posición inicial
        (i,j) hasta una posición en la que hay una salida.
        Entradas:
             -(i, j) : posición inicial a partir de donde
                      se realizará la búsqueda de un camino
                      hasta la posición de la salida.
             -laberinto : laberinto marcado con los caminos 
                        que se han recorrido hasta el momento
        Salidas:
             -Lista con las casillas, expresadas como pares
             ordenados, que llevan desde la posición inicial
             hasta la posición en que se encuentra la salida mas cercano.
             Si no existe un camino retorna la lista vacía.

             -Numero de pasos que se ha recorrido
    """
 
    if laberinto[i][j] == 3:
        return [[(i, j)],1]
 
    if laberinto[i][j] == 1:
        return [[],valorGrande]
 
    laberinto[i][j] = -1
 
    diferentesCaminos = []

    if i > 0 and laberinto[i - 1][j] in [0, 3]:                     # Arriba
        laberintoCopia = deepcopy(laberinto)
        camino = recorrido(i - 1, j, laberintoCopia)
        if camino: diferentesCaminos.append( [[(i, j)] + camino[0], camino[1]+1 ])
 
    if j < len(laberinto[i]) - 1 and laberinto[i][j + 1] in [0, 3]: # Derecha
        laberintoCopia = deepcopy(laberinto)
        camino = recorrido(i, j + 1, laberintoCopia)
        if camino: diferentesCaminos.append([ [(i, j)] + camino[0], camino[1]+1] )
 
    if i < len(laberinto) - 1 and laberinto[i + 1][j] in [0, 3]:    # Abajo
        laberintoCopia = deepcopy(laberinto)
        camino = recorrido(i + 1, j, laberintoCopia)
        if camino: diferentesCaminos.append( [[(i, j)] + camino[0], camino[1]+1] )
 
    if j > 0 and laberinto[i][j - 1] in [0, 3]:                     # Izquierda
        laberintoCopia = deepcopy(laberinto)
        camino = recorrido(i, j - 1, laberintoCopia)
        if camino: diferentesCaminos.append( [[(i, j)] + camino[0], camino[1]+1] )
 

    if len(diferentesCaminos)==0:
        return [[],valorGrande]
    else:
        return caminoMinimo(diferentesCaminos)
 

def caminoMinimo(caminos):
    minimo = [[],valorGrande]
    for camino in caminos:
        if (camino[1] < minimo[1]) and (camino[0] != []):
            minimo = [camino[0],camino[1]]
    return minimo


"""                 0  -------------->  j
                    |
                    |
                 i  |
                    |
                    V

0 - camino libre
1 - pared 
3 - posición de la salida

El laberinto debe ser recatangular
"""
valorGrande = 999999999
minimoGlobal = valorGrande

laberintoEntrada =  "11100000000003\n" + \
                    "00001111111111\n" + \
                    "01101111101111\n" + \
                    "01100000001111\n" + \
                    "01101111101110\n" + \
                    "01101111101110\n" + \
                    "30001000000000"
 

laberinto = creaLaberinto(laberintoEntrada)
impLab(laberinto)
print()

posicionInicial = [1,0]   # la posicion inicial de busqueda (i,j) <--------

caminoMasCorto = recorrido(posicionInicial[0],posicionInicial[1],laberinto)   

if caminoMasCorto[1] != valorGrande:
  print("El camino mas corto sigue el siguiente recorrido:")
  for x in caminoMasCorto[0] : 
      print(x)

  print()
  print("El camino mas corto tiene ",caminoMasCorto[1]," pasos")
else:
  print("No hay salida!")

input()