import os

import pygame
from pygame.locals import *

from ajedrez import Ajedrez
from eventos import Eventos


class Juego:
    def __init__(self):

        ancho_pantalla = 900
        largo_pantalla = 900

        self.menu_desplegado = False

        self.corriendo = True

        self.recursos = "res"


        pygame.display.init()

        pygame.font.init()


        self.pantalla = pygame.display.set_mode([ancho_pantalla, largo_pantalla])


        titulo_ventana = "Ajedrez"

        pygame.display.set_caption(titulo_ventana)


        icon_src = os.path.join(self.recursos, "chess_icon.png")

        icon = pygame.image.load(icon_src)

        pygame.display.set_icon(icon)

        pygame.display.flip()

        self.clock = pygame.time.Clock()

    def empezar_juego(self):

        self.posicionamiento_tablero_x = 140
        self.posicionamiento_tablero_y = 125
        self.dimensiones_tablero = (self.posicionamiento_tablero_x, self.posicionamiento_tablero_y)


        buscar_tablero = os.path.join(self.recursos, "board.png")

        self.imagen_tablero = pygame.image.load(buscar_tablero).convert()


        tamano_casilla = self.imagen_tablero.get_rect().width // 8


        self.localizacion_tablero = []


        for x in range(0, 8):
            self.localizacion_tablero.append([])
            for y in range(0, 8):
                self.localizacion_tablero[x].append([self.posicionamiento_tablero_x + (x * tamano_casilla),
                                                     self.posicionamiento_tablero_y + (y * tamano_casilla)])


        buscar_piezas = os.path.join(self.recursos, "pieces.png")

        self.ajedrez = Ajedrez(self.pantalla, buscar_piezas, self.localizacion_tablero, tamano_casilla)

        while self.corriendo:
            self.clock.tick(5)

            for event in pygame.event.get():

                key_pressed = pygame.key.get_pressed()

                if event.type == pygame.QUIT or key_pressed[K_ESCAPE]:
                    self.corriendo = False
                elif key_pressed[K_SPACE]:
                    self.ajedrez.resetear()

            winner = self.ajedrez.ganador

            if not self.menu_desplegado:
                self.menu()
            elif len(winner) > 0:
                self.declarar_ganador(winner)
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

        texto_bienvenida = FUENTE_GRANDE.render("Ajedrez", False, color_negro)
        proyecto = FUENTE_PEQUENA.render("entrega final, APOO", True, color_negro)
        label_boton_inicio = FUENTE_PEQUENA.render("Jugar", True, color_blanco)

        self.pantalla.blit(texto_bienvenida,
                           ((self.pantalla.get_width() - texto_bienvenida.get_width()) // 2,
                            150))

        self.pantalla.blit(proyecto,
                           ((self.pantalla.get_width() - proyecto.get_width()) // 2,
                            self.pantalla.get_height() - proyecto.get_height() - 100))

        self.pantalla.blit(label_boton_inicio,
                           ((boton_inicio.x + (boton_inicio.width - label_boton_inicio.get_width()) // 2,
                             boton_inicio.y + (boton_inicio.height - label_boton_inicio.get_height()) // 2)))

        tecla_presionada = pygame.key.get_pressed()

        evento = Eventos()

        if evento.click_izquierdo():
            coordenadas_mouse = evento.get_mouse()

            if boton_inicio.collidepoint(coordenadas_mouse[0], coordenadas_mouse[1]):
                pygame.draw.rect(self.pantalla, color_blanco, boton_inicio, 3)
                self.menu_desplegado = True

            elif tecla_presionada[K_RETURN]:
                self.menu_desplegado = True

    def juego(self):

        color = (0, 0, 0)

        self.pantalla.fill(color)

        self.pantalla.blit(self.imagen_tablero, self.dimensiones_tablero)

        self.ajedrez.jugar_turno()

        self.ajedrez.dibujar_piezas()

    def declarar_ganador(self, ganador):

        color_fondo = (255, 255, 255)

        self.pantalla.fill(color_fondo)

        color_negro = (0, 0, 0)

        boton_resetear = pygame.Rect(250, 300, 140, 50)

        pygame.draw.rect(self.pantalla, color_negro, boton_resetear)

        color_blanco = (255, 255, 255)

        fuente_grande = pygame.font.SysFont("Cooper black", 50)
        fuente_pequena = pygame.font.SysFont("Cooper black", 20)

        # text to show winner
        texto = ganador + " gana!"
        texto_ganador = fuente_grande.render(texto, False, color_negro)


        label_de_reset = "Juega de nuevo"
        boton_label_reset = fuente_pequena.render(label_de_reset, True, color_blanco)

        # show winner text
        self.pantalla.blit(texto_ganador,
                           ((self.pantalla.get_width() - texto_ganador.get_width()) // 2,
                            150))


        self.pantalla.blit(boton_label_reset,
                           ((boton_resetear.x + (boton_resetear.width - boton_label_reset.get_width()) // 2,
                             boton_resetear.y + (boton_resetear.height - boton_label_reset.get_height()) // 2)))


        tecla_presionada = pygame.key.get_pressed()

        eventos = Eventos()


        if eventos.click_izquierdo():

            coordenadas_mouse = eventos.get_mouse()


            if boton_resetear.collidepoint(coordenadas_mouse[0], coordenadas_mouse[1]):

                pygame.draw.rect(self.pantalla, color_blanco, boton_resetear, 3)


                self.menu_desplegado = False

            elif tecla_presionada[K_RETURN]:
                self.menu_desplegado = False

            self.ajedrez.resetear()

            self.ajedrez.ganador = ""
