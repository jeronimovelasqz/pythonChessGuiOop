import pygame
import random
from pieza import Pieza
from eventos import Eventos


class Ajedrez(object):
    def __init__(self, pantalla, buscar_piezas, coordenadas_cuadrado, tamano_cuadrado):

        self.pantalla = pantalla

        self.piezas_ajedrez = Pieza(buscar_piezas, columnas=6, filas=2)

        self.localizacion_tablero = coordenadas_cuadrado

        self.tamano_cuadrado = tamano_cuadrado

        self.turno = {"black": 0,
                      "white": 0}

        # list containing possible moves for the selected piece
        self.movimientos = []
        #
        self.evento = Eventos()

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


        self.capturado = []

        self.ganador = ""

        self.resetear()

    def resetear(self):

        self.movimientos = []

        x = random.randint(0, 1)
        if x == 1:
            self.turno["black"] = 1
        elif x == 0:
            self.turno["white"] = 1

        self.localizacion_piezas = {}
        x = 0
        for i in range(97, 105):
            a = 8
            y = 0
            self.localizacion_piezas[chr(i)] = {}
            while a > 0:
                self.localizacion_piezas[chr(i)][a] = ["", False, [x, y]]
                a = a - 1
                y = y + 1
            x = x + 1

        for i in range(97, 105):
            x = 8
            while x > 0:
                if x == 8:
                    if chr(i) == 'a' or chr(i) == 'h':
                        self.localizacion_piezas[chr(i)][x][0] = "black_rook"
                    elif chr(i) == 'b' or chr(i) == 'g':
                        self.localizacion_piezas[chr(i)][x][0] = "black_knight"
                    elif chr(i) == 'c' or chr(i) == 'f':
                        self.localizacion_piezas[chr(i)][x][0] = "black_bishop"
                    elif chr(i) == 'd':
                        self.localizacion_piezas[chr(i)][x][0] = "black_queen"
                    elif chr(i) == 'e':
                        self.localizacion_piezas[chr(i)][x][0] = "black_king"
                elif x == 7:
                    self.localizacion_piezas[chr(i)][x][0] = "black_pawn"
                elif x == 2:
                    self.localizacion_piezas[chr(i)][x][0] = "white_pawn"
                elif x == 1:
                    if chr(i) == 'a' or chr(i) == 'h':
                        self.localizacion_piezas[chr(i)][x][0] = "white_rook"
                    elif chr(i) == 'b' or chr(i) == 'g':
                        self.localizacion_piezas[chr(i)][x][0] = "white_knight"
                    elif chr(i) == 'c' or chr(i) == 'f':
                        self.localizacion_piezas[chr(i)][x][0] = "white_bishop"
                    elif chr(i) == 'd':
                        self.localizacion_piezas[chr(i)][x][0] = "white_queen"
                    elif chr(i) == 'e':
                        self.localizacion_piezas[chr(i)][x][0] = "white_king"
                x = x - 1


    def jugar_turno(self):

        color_blanco = (255, 255, 255)

        fuente_pequena = pygame.font.SysFont("Cooper black", 20)

        if self.turno["black"]:
            turno_texto = fuente_pequena.render("Turno: Negras", True, color_blanco)
        elif self.turno["white"]:
            turno_texto = fuente_pequena.render("Turno: Blancas", True, color_blanco)

        self.pantalla.blit(turno_texto,
                           ((self.pantalla.get_width() - turno_texto.get_width()) // 2,
                            50))

        if self.turno["black"]:
            self.mover_pieza("black")

        elif self.turno["white"]:
            self.mover_pieza("white")

    def dibujar_piezas(self):
        verde_transparente = (0, 194, 39, 170)
        azul_transparente = (28, 21, 212, 170)
        rojo_transparente = (255, 0, 0, 170)

        # create a transparent superficies
        superficies = pygame.Surface((self.tamano_cuadrado, self.tamano_cuadrado), pygame.SRCALPHA)
        superficies.fill(rojo_transparente)

        superficie_2 = pygame.Surface((self.tamano_cuadrado, self.tamano_cuadrado), pygame.SRCALPHA)
        superficie_2.fill(verde_transparente)

        for val in self.localizacion_piezas.values():
            for valor in val.values():
                nombre_pieza = valor[0]
                coordenada_pieza_x, coordenada_pieza_y = valor[2]

                if valor[1] and len(valor[0]) > 5:

                    if valor[0][:5] == "black":
                        self.pantalla.blit(superficies,
                                           self.localizacion_tablero[coordenada_pieza_x][coordenada_pieza_y])
                        if len(self.movimientos) > 0:
                            for move in self.movimientos:
                                coordenadas_x = move[0]
                                coordenada_y = move[1]
                                if 0 <= coordenadas_x < 8 and 0 <= coordenada_y < 8:
                                    self.pantalla.blit(superficies,
                                                       self.localizacion_tablero[coordenadas_x][coordenada_y])

                    elif valor[0][:5] == "white":
                        self.pantalla.blit(superficie_2,
                                           self.localizacion_tablero[coordenada_pieza_x][coordenada_pieza_y])
                        if len(self.movimientos) > 0:
                            for move in self.movimientos:
                                coordenadas_x = move[0]
                                coordenada_y = move[1]
                                if 0 <= coordenadas_x < 8 and 0 <= coordenada_y < 8:
                                    self.pantalla.blit(superficie_2,
                                                       self.localizacion_tablero[coordenadas_x][coordenada_y])


        for val in self.localizacion_piezas.values():
            for valor in val.values():

                nombre_pieza = valor[0]

                coordenada_pieza_x, coordenada_pieza_y = valor[2]

                if len(valor[0]) > 1:
                    # draw piece on the board
                    self.piezas_ajedrez.dibujar(self.pantalla, nombre_pieza,
                                             self.localizacion_tablero[coordenada_pieza_x][coordenada_pieza_y])

    def movimientos_posibles(self, nombre_pieza, piece_coord):

        posiciones = []

        if len(nombre_pieza) > 0:

            coordenada_x, coordenada_y = piece_coord

            if nombre_pieza[6:] == "bishop":
                posiciones = self.movientos_diagonal(posiciones, nombre_pieza, piece_coord)


            elif nombre_pieza[6:] == "pawn":

                numero_columnas = chr(97 + coordenada_x)
                numero_fila = 8 - coordenada_y

                if nombre_pieza == "black_pawn":
                    if coordenada_y + 1 < 8:

                        numero_fila = numero_fila - 1
                        pieza_frontal = self.localizacion_piezas[numero_columnas][numero_fila][0]

                        if pieza_frontal[6:] != "pawn":
                            posiciones.append([coordenada_x, coordenada_y + 1])

                            if coordenada_y < 2:
                                posiciones.append([coordenada_x, coordenada_y + 2])

                        if coordenada_x - 1 >= 0 and coordenada_y + 1 < 8:
                            x = coordenada_x - 1
                            y = coordenada_y + 1

                            numero_columnas = chr(97 + x)
                            numero_fila = 8 - y
                            a_capturar = self.localizacion_piezas[numero_columnas][numero_fila]

                            if a_capturar[0][:5] == "white":
                                posiciones.append([x, y])

                        if coordenada_x + 1 < 8 and coordenada_y + 1 < 8:
                            x = coordenada_x + 1
                            y = coordenada_y + 1

                            numero_columnas = chr(97 + x)
                            numero_fila = 8 - y
                            a_capturar = self.localizacion_piezas[numero_columnas][numero_fila]

                            if a_capturar[0][:5] == "white":
                                posiciones.append([x, y])


                elif nombre_pieza == "white_pawn":
                    if coordenada_y - 1 >= 0:

                        numero_fila = numero_fila + 1
                        pieza_frontal = self.localizacion_piezas[numero_columnas][numero_fila][0]

                        if pieza_frontal[6:] != "pawn":
                            posiciones.append([coordenada_x, coordenada_y - 1])
                            # black pawns can move two posiciones ahead for first move
                            if coordenada_y > 5:
                                posiciones.append([coordenada_x, coordenada_y - 2])

                        if coordenada_x - 1 >= 0 and coordenada_y - 1 >= 0:
                            x = coordenada_x - 1
                            y = coordenada_y - 1

                            numero_columnas = chr(97 + x)
                            numero_fila = 8 - y
                            a_capturar = self.localizacion_piezas[numero_columnas][numero_fila]

                            if a_capturar[0][:5] == "black":
                                posiciones.append([x, y])

                        if coordenada_x + 1 < 8 and coordenada_y - 1 >= 0:
                            x = coordenada_x + 1
                            y = coordenada_y - 1

                            numero_columnas = chr(97 + x)
                            numero_fila = 8 - y
                            a_capturar = self.localizacion_piezas[numero_columnas][numero_fila]

                            if a_capturar[0][:5] == "black":
                                posiciones.append([x, y])



            elif nombre_pieza[6:] == "rook":

                posiciones = self.movimientos_lineales(posiciones, nombre_pieza, piece_coord)


            elif nombre_pieza[6:] == "knight":

                if (coordenada_x - 2) >= 0:
                    if (coordenada_y - 1) >= 0:
                        posiciones.append([coordenada_x - 2, coordenada_y - 1])
                    if (coordenada_y + 1) < 8:
                        posiciones.append([coordenada_x - 2, coordenada_y + 1])

                if (coordenada_y - 2) >= 0:
                    if (coordenada_x - 1) >= 0:
                        posiciones.append([coordenada_x - 1, coordenada_y - 2])
                    if (coordenada_x + 1) < 8:
                        posiciones.append([coordenada_x + 1, coordenada_y - 2])

                if (coordenada_x + 2) < 8:
                    if (coordenada_y - 1) >= 0:
                        posiciones.append([coordenada_x + 2, coordenada_y - 1])
                    if (coordenada_y + 1) < 8:
                        posiciones.append([coordenada_x + 2, coordenada_y + 1])

                if (coordenada_y + 2) < 8:
                    if (coordenada_x - 1) >= 0:
                        posiciones.append([coordenada_x - 1, coordenada_y + 2])
                    if (coordenada_x + 1) < 8:
                        posiciones.append([coordenada_x + 1, coordenada_y + 2])


            elif nombre_pieza[6:] == "king":
                if (coordenada_y - 1) >= 0:
                    posiciones.append([coordenada_x, coordenada_y - 1])

                if (coordenada_y + 1) < 8:
                    posiciones.append([coordenada_x, coordenada_y + 1])

                if (coordenada_x - 1) >= 0:

                    posiciones.append([coordenada_x - 1, coordenada_y])

                    if (coordenada_y - 1) >= 0:
                        posiciones.append([coordenada_x - 1, coordenada_y - 1])

                    if (coordenada_y + 1) < 8:
                        posiciones.append([coordenada_x - 1, coordenada_y + 1])

                if (coordenada_x + 1) < 8:

                    posiciones.append([coordenada_x + 1, coordenada_y])

                    if (coordenada_y - 1) >= 0:
                        posiciones.append([coordenada_x + 1, coordenada_y - 1])

                    if (coordenada_y + 1) < 8:
                        posiciones.append([coordenada_x + 1, coordenada_y + 1])


            elif nombre_pieza[6:] == "queen":

                posiciones = self.movientos_diagonal(posiciones, nombre_pieza, piece_coord)

                # find linear moves
                posiciones = self.movimientos_lineales(posiciones, nombre_pieza, piece_coord)

            para_remover = []

            for pos in posiciones:
                x, y = pos

                numero_columnas = chr(97 + x)
                numero_fila = 8 - y

                des_piece_name = self.localizacion_piezas[numero_columnas][numero_fila][0]
                if des_piece_name[:5] == nombre_pieza[:5]:
                    para_remover.append(pos)

            for i in para_remover:
                posiciones.remove(i)

        return posiciones

    def mover_pieza(self, turno):

        cuadrado = self.obtener_cuadrado_seleccionado()

        if cuadrado:

            nombre_pieza = cuadrado[0]

            color_pieza = nombre_pieza[:5]

            numero_columna = cuadrado[1]

            numero_fila = cuadrado[2]

            x, y = self.localizacion_piezas[numero_columna][numero_fila][2]

            if (len(nombre_pieza) > 0) and (color_pieza == turno):
                self.movimientos = self.movimientos_posibles(nombre_pieza, [x, y])

            p = self.localizacion_piezas[numero_columna][numero_fila]

            for i in self.movimientos:
                if i == [x, y]:
                    if (p[0][:5] == turno) or len(p[0]) == 0:
                        self.validar_movimiento([x, y])
                    else:
                        self.capturar_pieza(turno, [numero_columna, numero_fila], [x, y])

            if color_pieza == turno:

                for k in self.localizacion_piezas.keys():
                    for key in self.localizacion_piezas[k].keys():
                        self.localizacion_piezas[k][key][1] = False

                self.localizacion_piezas[numero_columna][numero_fila][1] = True

    def obtener_cuadrado_seleccionado(self):

        click_izquierdo = self.evento.click_izquierdo()

        if click_izquierdo:

            evento_mouse = self.evento.get_mouse()

            for i in range(len(self.localizacion_tablero)):
                for j in range(len(self.localizacion_tablero)):
                    rect = pygame.Rect(self.localizacion_tablero[i][j][0], self.localizacion_tablero[i][j][1],
                                       self.tamano_cuadrado, self.tamano_cuadrado)
                    collision = rect.collidepoint(evento_mouse[0], evento_mouse[1])
                    if collision:
                        selected = [rect.x, rect.y]

                        for k in range(len(self.localizacion_tablero)):

                            try:
                                prueba = None
                                prueba = self.localizacion_tablero[k].index(selected)
                                if prueba is not None:

                                    for val in self.localizacion_piezas.values():
                                        for value in val.values():
                                            if not value[1]:
                                                value[1] = False


                                    numero_columna = chr(97 + k)
                                    numero_fila = 8 - prueba

                                    nombre_pieza = self.localizacion_piezas[numero_columna][numero_fila][0]

                                    return [nombre_pieza, numero_columna, numero_fila]
                            except:
                                pass
        else:
            return None

    def capturar_pieza(self, turno, coordenadas_tablero, coordenadas_pieza):

        x, y = coordenadas_pieza


        numero_columna, numero_fila = coordenadas_tablero

        p = self.localizacion_piezas[numero_columna][numero_fila]

        if p[0] == "white_king":
            self.ganador = "Black"
            print("negras ganan")
        elif p[0] == "black_king":
            self.ganador = "White"
            print("blancas ganan")


        self.capturado.append(p)

        self.validar_movimiento(coordenadas_pieza)

    def validar_movimiento(self, destination):
        destino_numero_columna = chr(97 + destination[0])
        destino_numero_fila = 8 - destination[1]

        for k in self.localizacion_piezas.keys():
            for key in self.localizacion_piezas[k].keys():
                pieza_tablero = self.localizacion_piezas[k][key]

                if pieza_tablero[1]:

                    self.localizacion_piezas[k][key][1] = False

                    nombre_pieza = self.localizacion_piezas[k][key][0]

                    self.localizacion_piezas[destino_numero_columna][destino_numero_fila][0] = nombre_pieza

                    buscar_nombre = self.localizacion_piezas[k][key][0]

                    self.localizacion_piezas[k][key][0] = ""

                    # change turn
                    if self.turno["black"]:
                        self.turno["black"] = 0
                        self.turno["white"] = 1
                    elif "white":
                        self.turno["black"] = 1
                        self.turno["white"] = 0

                    buscar_localizacion = k + str(key)
                    destino_localizacion = destino_numero_columna + str(destino_numero_fila)
                    print("{} se movio desde {} a {}".format(buscar_nombre, buscar_localizacion, destino_localizacion))


    def movientos_diagonal(self, posiciones, nombre_pieza, coordenada_pieza):

        x, y = coordenada_pieza

        while True:
            x = x - 1
            y = y - 1
            if x < 0 or y < 0:
                break
            else:
                posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while True:
            x = x + 1
            y = y + 1
            if x > 7 or y > 7:
                break
            else:
                posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while True:
            x = x - 1
            y = y + 1
            if x < 0 or y > 7:
                break
            else:
                posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while True:
            x = x + 1
            y = y - 1
            if x > 7 or y < 0:
                break
            else:
                posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break

        return posiciones


    def movimientos_lineales(self, posiciones, nombre_pieza, coordenada_pieza):

        x, y = coordenada_pieza

        while x > 0:
            x = x - 1
            posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while x < 7:
            x = x + 1
            posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while y > 0:
            y = y - 1
            posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while y < 7:
            y = y + 1
            posiciones.append([x, y])


            numero_columna = chr(97 + x)
            numero_fila = 8 - y
            p = self.localizacion_piezas[numero_columna][numero_fila]


            if len(p[0]) > 0 and nombre_pieza[:5] != p[:5]:
                break

        return posiciones
