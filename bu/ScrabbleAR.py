import json
import time
import PySimpleGUI as sg
from ScoreControl import ScoreControl as sc
from ModuloAtril import *
from Tableros import *
from LoadGame import *
from Interfaz import *
import VerificadorPalabra as verif


def Tablero(window, matriz_tablero, nivel):
    puntos = sc(0)
    mano_jugador = []
    mano_cpu = []
    #jugador = Atril(mano_jugador)
    lista_de_posiciones=[]
    jugador=Atril(['H','O','L','A','U','B','E'])
    cpu = Atril(mano_cpu)
    jugador.repartirFichas()
    cpu.repartirFichas()
    ActualizarFichas(window,jugador,cpu)
    while True:
        event, values = window.Read()
        if (event == 'TERMINAR') | (event == None):
            break;
        elif event == 'POSPONER':
            GuardarPartida(matriz_tablero, nivel)
            sg.Popup('Partida guardada en el archivo')
        elif event == 'TOP 10':
            sg.Popup('En Mantenimiento')
        elif event =='REGLAS':
            InterfazReglas(nivel)
        elif(('J' in event) & (len(event) == 2)):
            letra_turno = window.Element(event).GetText()
            event, values = window.Read()
            if len(event) != 2:
                lista_de_posiciones.append(event)
                matriz_tablero[event]['letra'] = letra_turno
                window.Element(event).Update(letra_turno)
        if event == 'Fin De Turno':
            print('entre al evento')
            orientacion=verif.checkOrientation(lista_de_posiciones)
            #if orientacion == 'Vertical':
            if (verif.checkOrientation(lista_de_posiciones) == 'Vertical'):
                lista_de_posiciones.sort(key=lambda tup: int(tup[0]))  #Ordeno las posiciones por columna
                print('La palabra es en sentido vertical')
            else:
                lista_de_posiciones.sort(key=lambda tup: int(tup[2]))  #Ordeno la lista por fila
                print('La palabra es en sentido horizontal')
            word=verif.checkWord(lista_de_posiciones,matriz_tablero)
            print(word)
            verif.verifyWord(word)
            lista_de_posiciones=[]


        if event in matriz_tablero:
            puntos.multiplicar(matriz_tablero[event]['color_casilla'])
            print(puntos.get_puntos)


def Jugar(opcion):
    if opcion == 'Iniciar':
        nivel = Dificultad()
        if nivel == 'Facil':
            window, matriz_tablero, nivel = TableroFacil()
        elif nivel == 'Medio':
            window, matriz_tablero, nivel = TableroMedio()
        elif nivel == 'Dificil':
            window, matriz_tablero, nivel = TableroDificil()
        elif nivel == 'Personalizado':
            event, values = MenuPersonalizado()
            window, matriz_tablero, nivel = TableroPersonalizado(values['Nivel'])
        Tablero(window, matriz_tablero, nivel)
    elif opcion == 'Cargar Partida':
        window, matriz_tablero, nivel = CargarPartida()
        Tablero(window, matriz_tablero, nivel)


Jugar(MenuPrincipal())
