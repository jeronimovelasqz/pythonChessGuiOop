import pygame


class Pieza(pygame.sprite.Sprite):

    def __init__(self, filename, columnas, filas):
        pygame.sprite.Sprite.__init__(self)
        self.piezas = {
            "peon_blanco": 5,
            "caballo_blanco": 3,
            "alfil_blanco": 2,
            "torre_blanco": 4,
            "rey_blanco": 0,
            "reina_blanco": 1,
            "peon_negro": 11,
            "caballo_negro": 9,
            "alfil_negro": 8,
            "torre_negro": 10,
            "rey_negro": 6,
            "reina_negro": 7
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

