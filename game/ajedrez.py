import pygame
import random
from pieza import Pieza
from eventos import Eventos


class Ajedrez(object):

    def __init__(self, pantalla, buscar_piezas, coordenas_cuadrado, tamano_cuadrado):
        self.pantalla = pantalla

        self.piezas_ajedrez = Pieza(buscar_piezas, columnas=6, filas=6)

        self.localizacion_tablero = coordenas_cuadrado

        self.tamano_cuadrado = tamano_cuadrado

        self.turno = {"negras": 0,
                      "blancas": 0}

        self.movimientos = []

        self.eventos = Eventos()

        self.piezas = {
            "peon_blanco": 5,
            "caballo_blanco": 3,
            "alfil_blanco": 2,
            "torre_blanca": 4,
            "rey_blanco": 0,
            "reina_blanca": 1,
            "peon_negro": 11,
            "caballo_negro": 9,
            "alfil_negro": 8,
            "torre_negra": 10,
            "rey_negro": 6,
            "reina_negra": 7
        }

        self.capturado = []

        self.ganador = ""

        self.reset()

    def reset(self):
        self.movimientos = []

        x = random.randint(0, 1)

        if x == 1:
            self.turno["negras"] = 1

        elif x == 0:
            self.turno["blancas"] = 1

        self.localizacion_pieza = {}

        x = 0

        for i in range(97, 105):
            a = 8
            y = 0
            self.localizacion_pieza[chr(i)] = {}
            while a > 0:
                self.localizacion_pieza[chr(i)][a] = ["", False, [x, y]]
                a = a - 1
                y = y + 1
            x = x + 1

        for i in range(97, 105):
            x = 8
            while x > 0:
                if x == 8:
                    if chr(i) == 'a' or chr(i) == 'h':
                        self.localizacion_pieza[chr(i)][x][0] = "torre_negra"
                    elif chr(i) == 'b' or chr(i) == 'g':
                        self.localizacion_pieza[chr(i)][x][0] = "caballo_negro"
                    elif chr(i) == 'c' or chr(i) == 'f':
                        self.localizacion_pieza[chr(i)][x][0] = "alfil_negro"
                    elif chr(i) == 'd':
                        self.localizacion_pieza[chr(i)][x][0] = "reina_negra"
                    elif chr(i) == 'e':
                        self.localizacion_pieza[chr(i)][x][0] = "rey_negro"
                elif x == 7:
                    self.localizacion_pieza[chr(i)][x][0] = "peon_negro"
                elif x == 2:
                    self.localizacion_pieza[chr(i)][x][0] = "peon_blanco"

                elif x == 1:
                    if chr(i) == 'a' or chr(i) == 'h':
                        self.localizacion_pieza[chr(i)][x][0] = "white_rook"
                    elif chr(i) == 'b' or chr(i) == 'g':
                        self.localizacion_pieza[chr(i)][x][0] = "caballo_blanco"
                    elif chr(i) == 'c' or chr(i) == 'f':
                        self.localizacion_pieza[chr(i)][x][0] = "alfil_blanco"
                    elif chr(i) == 'd':
                        self.localizacion_pieza[chr(i)][x][0] = "reina_blanca"
                    elif chr(i) == 'e':
                        self.localizacion_pieza[chr(i)][x][0] = "rey_blanco"
                x = x - 1

    def jugar_turno(self):

        COLOR_BLANCO = (255, 255, 255)

        FUENTE_PEQUENA = pygame.SysFont("Cooper black", 20)

        if self.turno["negras"]:
            texto_de_turno = FUENTE_PEQUENA.render("Turno: Negras", True, COLOR_BLANCO)

        elif self.turno["blancas"]:
            texto_de_turno = FUENTE_PEQUENA.render("Turno: Blancas", True, COLOR_BLANCO)

        self.pantalla.blit(texto_de_turno,
                           ((self.pantalla.get_width()) - (texto_de_turno.get_width())) // 2, 50)

        if self.turno["negras"]:
            self.mover_pieza("negras")
