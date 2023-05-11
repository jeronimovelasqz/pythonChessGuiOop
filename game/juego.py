import os
import pygame
from pygame.locals import *
from pieza import Pieza
from ajedrez import Ajedrez
from eventos import Eventos


class Juego:

    def __init__(self):
        # dimensiones
        pantalla_ancho = 900
        pantalla_largo = 900

        # variable booleana para revisar estado del menu
        self.desplegar_menu = False
        # variable booleana para inicializar loop del juego
        self.corriendo = True
        # base de los recursos del programa
        self.recursos = "rec"

        # inicializa ventana
        pygame.display.init()
        # inicializa font para el texto
        pygame.font.init()

        # crea la ventana del juego
        self.pantalla = pygame.display.set_mode([pantalla_ancho, pantalla_largo])

        # titulo de la ventana
        titulo_ventana = "Ajedrez"
        # poner subtitulos de ventana
        pygame.display.set_caption(titulo_ventana)

        # obtener posicion del icono
        icon_src = os.path.join(self.recursos, "#####")
        # cargar icono
        icono = pygame.image.load(icon_src)
        # poner icono
        pygame.display.set_icon(icon_src)
        # actualizar pantalla
        pygame.display.flip()
        # poner tiempo reloj
        self.clock = pygame.time.Clock()


def empezar_juego(self):
    # donde se pondra el tablero en la ventana
    self.balance_pantalla_x = 140
    self.balance_pantalla_y = 125
    self.tablero.dimensiones = (self.balance_pantalla_x, self.balance_pantalla_y)

    # obtener location de la imagen del tablero
    tablero_src = os.path.join(self.recursos, "############")
    # cargar imagen
    self.imagen_tablero = pygame.image.load(tablero_src).convert()

    # obtener ancho de los cuadrados del tablero
    largo_cuadrado = self.imagen_tablero.get_rect().ancho // 8

    # inicializar lista de posiciones actuales del tablero
    self.localizaciones_tablero = []
