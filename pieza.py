import pygame


class Pieza(pygame.sprite.Sprite):

    def __init__(self, filename, columnas, filas):
        pygame.sprite.Sprite.__init__(self)
        self.piezas = {
            "white_pawn": 5,
            "white_knight": 3,
            "white_bishop": 2,
            "white_rook": 4,
            "white_king": 0,
            "white_queen": 1,
            "black_pawn": 11,
            "black_knight": 9,
            "black_bishop": 8,
            "black_rook": 10,
            "black_king": 6,
            "black_queen": 7
        }
        self.spritesheet = pygame.image.load(filename).convert_alpha()

        self.columnas = columnas
        self.filas = filas
        self.contar_casillas = columnas * filas

        self.rect = self.spritesheet.get_rect()
        ancho = self.casilla_ancho = self.rect.width // self.columnas
        largo = self.casilla_largo = self.rect.height // self.filas

        self.casillas = list([(i % columnas * ancho, i // columnas * largo, ancho, largo) for i in range(self.contar_casillas)])

    def dibujar(self, superficie, nombre_pieza, coordenadas):
        indice_pieza = self.piezas[nombre_pieza]
        superficie.blit(self.spritesheet, coordenadas, self.casillas[indice_pieza])

