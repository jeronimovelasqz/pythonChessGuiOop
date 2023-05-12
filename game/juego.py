import os

import pygame
from pygame.locals import *

from ajedrez import Ajedrez
from eventos import Eventos


def declarar_ganador(ganador):
    color_fondo = (255, 255, 255)


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
        self.res = "res"
        self.recursos = self.res

        # inicializa ventana
        pygame.display.init()
        # inicializa font para el texto
        pygame.font.init()

        # crea la ventana del juego
        self.pantalla = pygame.display.set_mode([pantalla_ancho, pantalla_largo])

        # titulo de la ventana
        titulo_ventana = "Ajedrez"
        # poner subtitles de ventana
        pygame.display.set_caption(titulo_ventana)

        # obtener posicion del icono
        icon_src = os.path.join(self.recursos, "../res/chess_icon.png")
        # cargar icono
        icono = pygame.image.load(icon_src)
        # poner icono
        pygame.display.set_icon(icono)
        # actualizar pantalla
        pygame.display.flip()
        # poner tiempo reloj
        self.clock = pygame.time.Clock()

    def empezar_juego(self):

        self.balance_tablero_x = 140
        self.balance_tablero_y = 125
        self.dimensiones_tablero = (self.balance_tablero_x, self.balance_tablero_y)

        buscar_tablero = os.path.join(self.recursos, "../res/board.png")

        self.imagen_tablero = pygame.image.load(buscar_tablero).convert()

        tamano_cuadrado = self.imagen_tablero.get_rect().width // 8

        self.localizacion_tablero = []

        for x in range(0, 8):
            self.localizacion_tablero.append([])
            for y in range(0, 8):
                self.localizacion_tablero[x].append([self.balance_tablero_x + (x * tamano_cuadrado),
                                                     self.balance_tablero_y + (y * tamano_cuadrado)])

        buscar_piezas = os.path.join(self.recursos, "../res/pieces.png")

        self.ajedrez = Ajedrez(self.pantalla, buscar_piezas, self.localizacion_tablero, tamano_cuadrado)

        while self.corriendo:
            self.clock.tick(5)

            for event in pygame.event.get():
                tecla_presionada = pygame.key.get_pressed()

                if event.type == pygame.QUIT or tecla_presionada[K_ESCAPE]:
                    self.corriendo = False

                elif tecla_presionada[K_SPACE]:
                    self.ajedrez.reset()

            ganador = self.ajedrez.ganador

            if not self.desplegar_menu:
                self.menu()

            elif len(ganador) > 0:
                self.declare_winner(ganador)

            else:
                self.juego()

            pygame.display.flip()

            pygame.event.pump()

        pygame.quit()

    def menu(self):

        color_fondo = (255, 255, 255)
        self.pantalla.fill(color_fondo)
        color_negro = (0, 0, 0)

        boton_inicio = pygame.Rect(270, 300, 100, 50)
        pygame.draw.rect(self.pantalla, color_negro, boton_inicio)

        color_blanco = (255, 255, 255)

        FUENTE_GRANDE = pygame.font.SysFont("Cooper black", 50)
        FUENTE_PEQUENA = pygame.font.SysFont("Cooper black", 20)

        TEXTO_BIENVENIDA = FUENTE_GRANDE.render("Chess", False, color_negro)
        PROYECTO = FUENTE_PEQUENA.render("entrega final, APOO", True, color_negro)
        LABEL_BOTON_EMPEZAR = FUENTE_PEQUENA.render("Jugar", True, color_blanco)

        self.pantalla.blit(PROYECTO,
                           ((self.pantalla.get_width() - TEXTO_BIENVENIDA.get_width()) // 2,
                            150))

        self.pantalla.blit(PROYECTO,
                           ((self.pantalla.get_width() - PROYECTO.get_width()) // 2,
                            self.pantalla.get_height() - PROYECTO.get_height() - 100))

        self.pantalla.blit(LABEL_BOTON_EMPEZAR,
                           ((boton_inicio.x + (boton_inicio.width - LABEL_BOTON_EMPEZAR.get_width()) // 2,
                             boton_inicio.y + (boton_inicio.height - LABEL_BOTON_EMPEZAR.get_height()) // 2)))

        tecla_presionada = pygame.key.get_pressed()

        evento = Eventos()

        if evento.click_izquierdo():

            coordenadas_mouse = evento.get_mouse()

            if boton_inicio.collidepoint(coordenadas_mouse[0], coordenadas_mouse[1]):

                pygame.draw.rect(self.pantalla, color_blanco, boton_inicio, 3)

                self.desplegar_menu = True

            elif tecla_presionada[K_RETURN]:
                self.desplegar_menu = True

    def juego(self):

        color = (0, 0, 0)

        self.pantalla.fill(color)

        # self.pantalla.blit(self.#, self.#)

        self.ajedrez.jugar_turno()

        self.ajedrez.dibujar_piezas()


    def declarar_ganador(self, ganador):

        color_fondo = (255, 255, 255)

        self.pantalla.fill(color_fondo)

        color_negro = (0, 0, 0)

        boton_resetear = pygame.Rect(250, 300, 140, 50)
        pygame.draw.rect(self.pantalla, color_negro, boton_resetear)

        color_blanco = (255, 255, 255)

        FUENTE_GRANDE = pygame.font.SysFont("Cooper black", 50)
        FUENTE_PEQUENA = pygame.font.SysFont("Cooper black", 20)

        texto = ganador + "gano"
        texto_ganador = FUENTE_GRANDE.render(texto, False, color_negro)

        label_reset = "Jugar de nuevo"
        boton_resetear_label = FUENTE_PEQUENA.render(label_reset, True, color_blanco)

        self.pantalla.blit(texto_ganador,
                         ((self.pantalla.get_width() - texto_ganador.get_width()) // 2,
                          150))


        self.pantalla.blit(boton_resetear_label,
                         ((boton_resetear.x + (boton_resetear.width - boton_resetear_label.get_width()) // 2,
                           boton_resetear.y + (boton_resetear.height - boton_resetear_label.get_height()) // 2)))



        tecla_presionada = pygame.key.get_pressed()
        util = Eventos()

        if util.click_izquierdo():

            coordenadas_mouse = util.get_mouse()


            if boton_resetear.collidepoint(coordenadas_mouse[0], coordenadas_mouse[1]):

                pygame.draw.rect(self.pantalla, color_blanco, boton_resetear, 3)
                self.desplegar_menu = False

            elif tecla_presionada[K_RETURN]:
                self.desplegar_menu = False

            self.ajedrez.reset()

            self.ajedrez.ganador = ""


