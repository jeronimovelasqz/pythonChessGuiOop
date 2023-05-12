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

    # calcular coordenadas de cada cuadro de juego

    for coordenada_x in range(0, 8):
        self.localizaciones_tablero.append([])
        for coordenada_y in range(0, 8):
            self.localizaciones_tablero[coordenada_x].append([self.balance_pantalla_x + (coordenada_x * largo_cuadrado),
                                                              self.balance_pantalla_y + (coordenada_y * largo_cuadrado)])


    # obtener localition de la imagen de cada pieza
    pieces_src = os.path.join(self.resources, "###########")

    self.ajedrez = Ajedrez(self.pantalla, pieces_src, self.localizaciones_tablero, largo_cuadrado)

    while self.corriendo:
        self.clock.tick(5)

        for evento in pygame.key.get_pressed():

            boton_presionado = pygame.key.get_pressed()

            if evento.type == pygame.QUIT or boton_presionado[K_ESCAPE]:

                self.corriendo = False

            elif boton_presionado[K_SPACE]:
                self.ajedrez.reset()

            ganador = self.ajedrez.ganador

            if not self.desplegar_menu:
                self.menu()

            elif len(ganador) > 0:
                self.declarar_ganador(ganador)

            else:
                self.juego()

            pygame.display.flip()

            pygame.event.pump()
        pygame.quit()


    def menu(self):

        color_fondo = (255, 255, 255)
        self.pantalla.fill(color_fondo)
        color_negro = (0, 0 ,0)

        boton_inicio = pygame.Rect(270, 300, 100, 50)
        pygame.draw.rect(self.pantalla, color_negro, boton_inicio)


        color_blanco = (255, 255, 255)

        FUENTE_GRANDE = pygame.font.SysFont("Cooper black", 50)
        FUENTE_PEQUENA = pygame.font.SysFont("Cooper black", 20)

        TEXTO_BIENVENIDA = FUENTE_GRANDE.render("Chess", False, color_negro)
        PROYECTO = FUENTE_PEQUENA.render("entrega final, APOO", True, color_negro)


        self.pantalla.blit(PROYECTO, (self.pantalla.ob)

