import pygame

from pieza import Pieza
from eventos import Eventos


class Ajedrez(object):

    def __init__(self, pantalla, buscar_piezas, coordenas_cuadrado, tamano_cuadrado):
        self.pantalla = pantalla

        self.piezas_ajedrez = Piece(buscar_piezas, columnas=6, filas=6)

        self.localizacion_tablero = coordenas_cuadrado

        self.tamano_cuadrado = tamano_cuadrado

        self.turno = {"negras":0,
                      "blancas":0}

        self.movimientos = []

        self.eventos = Eventos()


