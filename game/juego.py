import os
import pygame
from pygame.locals import *
from pieza import Pieza
from ajedrez import Ajedrez
from eventos import Eventos


class Juego:


    def __init__(self):

        pantalla_ancho = 900
        pantalla_largo = 900

        self.desplegar_menu = False

        self.corriendo = True

        self.recursos = "rec"

        pygame.display.init()
        pygame.font.init()

        self.pantalla = pygame.display.set_mode([pantalla_ancho, pantalla_largo])

        titulo_ventana = "Ajedrez"

        #icon_src = future image
        #OHLAS
