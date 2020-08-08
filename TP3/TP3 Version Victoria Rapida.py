from copy import deepcopy
from os import system, name 
import random
from time import sleep 
import time

def clear():  
    #if name == 'nt': 
    #    _ = system('cls')
    pass 

class Tablero:

    def __init__(self):
        self.tableroDib = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.tablero = [0,0,0,0,0,0,0,0,0]

    def dibujar(self):
            print('   |   |')
            print(' ' + self.tableroDib[0] + ' | ' + self.tableroDib[1] + ' | ' + self.tableroDib[2])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + self.tableroDib[3] + ' | ' + self.tableroDib[4] + ' | ' + self.tableroDib[5])
            print('   |   |')
            print('-----------')
            print('   |   |')
            print(' ' + self.tableroDib[6] + ' | ' + self.tableroDib[7] + ' | ' + self.tableroDib[8])
            print('   |   |')

    def jugar(self,jugada,jugador):
        self.tableroDib[jugada-1] = jugador.figura
        self.tablero[jugada-1] = jugador.numero


    def esGanador(self,jugador):
        num = jugador.numero
        return ((self.tablero[0] == num  and self.tablero[1] == num and self.tablero[2] == num) or # horizontal superior
        (self.tablero[3] == num and self.tablero[4] == num and self.tablero[5] == num) or # horizontal medio
        (self.tablero[6] == num and self.tablero[7] == num and self.tablero[8] == num) or # horizontal inferior
        (self.tablero[0] == num and self.tablero[3] == num and self.tablero[6] == num) or # vertical izquierda
        (self.tablero[1] == num and self.tablero[4] == num and self.tablero[7] == num) or # vertical medio
        (self.tablero[2] == num and self.tablero[5] == num and self.tablero[8] == num) or # vertical derecha
        (self.tablero[0] == num and self.tablero[4] == num and self.tablero[8] == num) or # diagonal
        (self.tablero[2] == num and self.tablero[4] == num and self.tablero[6] == num)) # diagonal

    def hayEspacioLibre(self):
        for e in self.tablero:
            if e == 0:
                return True

        return False

    def jugadasPosibles(self):
        posibles = []
        for i in range(0,9):
            if self.tablero[i]==0:
                posibles.append(i+1)
        return posibles

    def estaLibre(self,i):
        return self.tablero[i-1]==0

class Jugador:
    def __init__(self,numero,figura):
        self.numero = numero
        self.figura = figura

    def figura(self):
        return self.figura

    def numero(self):
        return self.numero

def jugadaJugador(tablero):
    jugada = -1
    while jugada<1 or jugada>9 or not tablero.estaLibre(jugada):
        print('¿Cuál es tu próxima jugada? [1-9]')
        jugada = int(input())
    return jugada

def jugadaComputadora(tablero,numero_jugada):
    start = time.time()

    # Las primeras jugadas no se calculan, se juega al medio o a la esquina 1 para jugar mas rapido
    if numero_jugada<3:
        if tablero.estaLibre(5):
            return 5
        else:
            return 1

    posibles = tablero.jugadasPosibles()            #Calculamos las jugadas posibles
    resultados = []
    for e in posibles:
        copTabl = deepcopy(tablero)
        resultados.append(mejorJugada(copTabl,e,0))   #Calculamos las valoraciones de las jugadas posibles

    print(posibles)
    print(resultados)

    pos = resultados.index(maximoYmenorProfundidad(resultados))         #Elegimos la que tiene el mejor resultado para la computadora

    end= time.time()
    print('Tiempo de calculo de jugada: ',end-start)

    return posibles[pos]

def mejorJugada(tablero,jugada,profundidad):

    tablero.jugar(jugada,computadora)

    if tablero.esGanador(computadora):          #Si gana la computadora, devolvemos resultado positivo
       return [10,profundidad]

    if not tablero.hayEspacioLibre():           #Si ya no quedan casillas disponibles, retorna empate
        return [0,profundidad]
    
    posibles = tablero.jugadasPosibles()
    resultados = []
    for e in posibles:
        copTabl = deepcopy(tablero)
        valor = mejorJugadaPersona(copTabl,e,profundidad+1)


        resultados.append(valor)    #Calculo las jugadas de la persona

    return minimoYmenorProfundidad(resultados)          #Supongo que elige la mejor para el

def mejorJugadaPersona(tablero,jugada,profundidad):    

    tablero.jugar(jugada,jugador)

    if tablero.esGanador(jugador):      #Si gana el jugador, devolvemos resultado negativo
        return [-10,profundidad]

    if not tablero.hayEspacioLibre():   #Si ya no quedan casillas disponibles, retorna empate
        return [0,profundidad]

    posibles = tablero.jugadasPosibles()
    resultados = []
    for e in posibles:
        copTabl = deepcopy(tablero)
        valor = mejorJugada(copTabl,e,profundidad+1)

        resultados.append(valor)    #Calculo las jugadas de la computadora
    
    return maximoYmenorProfundidad(resultados)          #Supongo que elige la mejor para ella

def maximoYmenorProfundidad(valores):
    minimo = -9999
    salida1 = []
    for valor in valores:
        if valor[0] > minimo:
            minimo = valor[0]
            salida1= [valor]
        elif valor[0] == minimo:
            salida1.append(valor)

    profundidadMinima = 99999
    for valor in salida1:
        if valor[1] < profundidadMinima:
            profundidadMinima = valor[1]
            salida2= valor
    
    return salida2

def minimoYmenorProfundidad(valores):
    maximo = 9999
    salida1 = []
    for valor in valores:
        if valor[0] < maximo:
            maximo = valor[0]
            salida1= [valor]
        elif valor[0] == maximo:
            salida1.append(valor)

    profundidadMinima = 99999
    for valor in salida1:
        if valor[1] < profundidadMinima:
            profundidadMinima = valor[1]
            salida2 = valor
    
    return salida2




# Crea el tablero
tabl = Tablero()

# Comienza Jugador  Humano = 1
#                   Computadora = 2
turno = random.randint(1, 2) 

# Crea los jugadores
if turno==1:
    jugador = Jugador(1,'X')
    computadora = Jugador(2,'O')
else:
    jugador = Jugador(1,'O')
    computadora = Jugador(2,'X')

# Inicia el juego
juegoEnCurso = True
numero_jugada = 1

while juegoEnCurso:

    if turno == 1:
    
        # Turno del jugador
        print('TURNO del jugador')
        tabl.dibujar()
        jugada = jugadaJugador(tabl)
        tabl.jugar(jugada,jugador)

        if tabl.esGanador(jugador):
            clear()
            print('Imposible...venciste a Skynet')
            print()
            tabl.dibujar()
            juegoEnCurso = False
            sleep(4)

        turno = 2

    else:

        # Turno de la computadora
        print('TURNO de la computadora')
        tab2=deepcopy(tabl)
        jugada = jugadaComputadora(tab2,numero_jugada)
        tabl.jugar(jugada,computadora)

        if tabl.esGanador(computadora):
            clear()
            print('PERDISTE, QUE TRISTE.')
            print()
            tabl.dibujar()
            juegoEnCurso = False
            sleep(2.5)

        turno = 1

    if not tabl.hayEspacioLibre():
        clear()
        print('EMPATE, BIEN JUGADO.')
        print()
        tabl.dibujar()
        juegoEnCurso = False
        sleep(2.5)
        
    clear()
    numero_jugada += 1



