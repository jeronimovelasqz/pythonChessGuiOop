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

        FUENTE_PEQUENA = pygame.font.SysFont("Cooper black", 20)

        if self.turno["negras"]:
            texto_de_turno = FUENTE_PEQUENA.render("Turno: Negras", True, COLOR_BLANCO)

        elif self.turno["blancas"]:
            texto_de_turno = FUENTE_PEQUENA.render("Turno: Blancas", True, COLOR_BLANCO)

        self.pantalla.blit(texto_de_turno,
                           ((self.pantalla.get_width()) - (texto_de_turno.get_width())) // 2, 50)

        if self.turno["negras"]:
            self.mover_pieza("negras")

        elif self.turno["blancas"]:
            self.mover_pieza("blancas")

    def dibujar_piezas(self):
        verde_transparente = (0, 194, 39, 170)
        rojo_transparente = (255, 0, 0, 170)

        superficie = pygame.Surface((self.tamano_cuadrado, self.tamano_cuadrado), pygame.SRCALPHA)
        superficie.fill(rojo_transparente)

        superficie_2 = pygame.Surface((self.tamano_cuadrado, self.tamano_cuadrado), pygame.SRCALPHA)
        superficie_2.fill(verde_transparente)

        for val in self.localizacion_pieza.values():
            for value in val.values():

                nombre_pieza = value[0]

                coordenada_pieza_x, coordenada_pieza_y = value[2]

                if value[1] and len(value[0]) > 5:

                    if value[0][:5] == "negras":
                        self.pantalla.blit(superficie,
                                           self.localizacion_tablero[coordenada_pieza_x][coordenada_pieza_y])
                        if len(self.movimientos) > 0:
                            for move in self.movimientos:
                                x_coordenada = move[0]
                                y_coordenada = move[1]
                                if 0 <= x_coordenada < 8 and 0 <= y_coordenada < 8:
                                    self.pantalla.blit(superficie,
                                                       self.localizacion_tablero[x_coordenada][y_coordenada])

                    elif value[0][:5] == "blancas":
                        self.pantalla.blit(superficie_2,
                                           self.localizacion_tablero[coordenada_pieza_x][coordenada_pieza_y])
                        if len(self.movimientos) > 0:
                            for move in self.movimientos:
                                x_coordenada = move[0]
                                y_coordenada = move[1]
                                if 0 <= x_coordenada < 8 and 0 <= y_coordenada < 8:
                                    self.pantalla.blit(superficie_2,
                                                       self.localizacion_tablero[x_coordenada][y_coordenada])

        for val in self.localizacion_pieza.values():
            for value in val.values():
                nombre_pieza = value[0]
                coordenada_pieza_x, coordenada_pieza_y = value[2]
                if len(value[0]) > 1:
                    self.piezas_ajedrez.dibujar(self.pantalla, nombre_pieza,
                                                self.localizacion_tablero[coordenada_pieza_x][coordenada_pieza_y])

    def movimientos_posibles(self, nombre_pieza, coordenada_pieza):

        positions = []

        if len(nombre_pieza) > 0:

            coordenada_x, coordenada_y = coordenada_pieza

            if nombre_pieza[6:] == "bishop":
                positions = self.diagonal_moves(positions, nombre_pieza, coordenada_pieza)


            elif nombre_pieza[6:] == "peon":

                numero_columna = chr(97 + coordenada_x)
                numero_fila = 8 - coordenada_y

                if nombre_pieza == "peon_negro":
                    if coordenada_y + 1 < 8:

                        numero_fila = numero_fila - 1
                        front_piece = self.localizacion_pieza[numero_columna][numero_fila][0]

                        if front_piece[6:] != "peon":
                            positions.append([coordenada_x, coordenada_y + 1])

                            if coordenada_y < 2:
                                positions.append([coordenada_x, coordenada_y + 2])

                        if coordenada_x - 1 >= 0 and coordenada_y + 1 < 8:
                            x = coordenada_x - 1
                            y = coordenada_y + 1

                            numero_columna = chr(97 + x)
                            numero_fila = 8 - y
                            to_capture = self.localizacion_pieza[numero_columna][numero_fila]

                            if to_capture[0][:5] == "blanco":
                                positions.append([x, y])

                        if coordenada_x + 1 < 8 and coordenada_y + 1 < 8:
                            x = coordenada_x + 1
                            y = coordenada_y + 1

                            numero_columna = chr(97 + x)
                            numero_fila = 8 - y
                            to_capture = self.localizacion_pieza[numero_columna][numero_fila]

                            if to_capture[0][:5] == "blanco":
                                positions.append([x, y])


                elif nombre_pieza == "peon_blanco":
                    if coordenada_y - 1 >= 0:

                        numero_fila = numero_fila + 1
                        front_piece = self.localizacion_pieza[numero_columna][numero_fila][0]

                        if front_piece[6:] != "peon":
                            positions.append([coordenada_x, coordenada_y - 1])

                            if coordenada_y > 5:
                                positions.append([coordenada_x, coordenada_y - 2])

                        if coordenada_x - 1 >= 0 and coordenada_y - 1 >= 0:
                            x = coordenada_x - 1
                            y = coordenada_y - 1

                            numero_columna = chr(97 + x)
                            numero_fila = 8 - y
                            to_capture = self.localizacion_pieza[numero_columna][numero_fila]

                            if to_capture[0][:5] == "negro":
                                positions.append([x, y])

                        if coordenada_x + 1 < 8 and coordenada_y - 1 >= 0:
                            x = coordenada_x + 1
                            y = coordenada_y - 1

                            numero_columna = chr(97 + x)
                            numero_fila = 8 - y
                            to_capture = self.localizacion_pieza[numero_columna][numero_fila]

                            if to_capture[0][:5] == "negro":
                                positions.append([x, y])



            elif nombre_pieza[6:] == "torre":
                # find linear moves
                positions = self.linear_moves(positions, nombre_pieza, coordenada_pieza)


            elif nombre_pieza[6:] == "caballo":

                if (coordenada_x - 2) >= 0:
                    if (coordenada_y - 1) >= 0:
                        positions.append([coordenada_x - 2, coordenada_y - 1])
                    if (coordenada_y + 1) < 8:
                        positions.append([coordenada_x - 2, coordenada_y + 1])

                if (coordenada_y - 2) >= 0:
                    if (coordenada_x - 1) >= 0:
                        positions.append([coordenada_x - 1, coordenada_y - 2])
                    if (coordenada_x + 1) < 8:
                        positions.append([coordenada_x + 1, coordenada_y - 2])

                if (coordenada_x + 2) < 8:
                    if (coordenada_y - 1) >= 0:
                        positions.append([coordenada_x + 2, coordenada_y - 1])
                    if (coordenada_y + 1) < 8:
                        positions.append([coordenada_x + 2, coordenada_y + 1])

                if (coordenada_y + 2) < 8:
                    if (coordenada_x - 1) >= 0:
                        positions.append([coordenada_x - 1, coordenada_y + 2])
                    if (coordenada_x + 1) < 8:
                        positions.append([coordenada_x + 1, coordenada_y + 2])


            elif nombre_pieza[6:] == "rey":
                if (coordenada_y - 1) >= 0:
                    # top spot
                    positions.append([coordenada_x, coordenada_y - 1])

                if (coordenada_y + 1) < 8:
                    # bottom spot
                    positions.append([coordenada_x, coordenada_y + 1])

                if (coordenada_x - 1) >= 0:
                    # left spot
                    positions.append([coordenada_x - 1, coordenada_y])
                    # top left spot
                    if (coordenada_y - 1) >= 0:
                        positions.append([coordenada_x - 1, coordenada_y - 1])
                    # bottom left spot
                    if (coordenada_y + 1) < 8:
                        positions.append([coordenada_x - 1, coordenada_y + 1])

                if (coordenada_x + 1) < 8:
                    # right spot
                    positions.append([coordenada_x + 1, coordenada_y])
                    # top right spot
                    if (coordenada_y - 1) >= 0:
                        positions.append([coordenada_x + 1, coordenada_y - 1])
                    # bottom right spot
                    if (coordenada_y + 1) < 8:
                        positions.append([coordenada_x + 1, coordenada_y + 1])


            elif nombre_pieza[6:] == "reina":

                positions = self.diagonal_moves(positions, nombre_pieza, coordenada_pieza)

                positions = self.linear_moves(positions, nombre_pieza, coordenada_pieza)

            para_remover = []

            for pos in positions:
                x, y = pos

                numero_columna = chr(97 + x)
                numero_fila = 8 - y

                des_piece_name = self.localizacion_pieza[numero_columna][numero_fila][0]
                if des_piece_name[:5] == nombre_pieza[:5]:
                    para_remover.append(pos)

            for i in para_remover:
                positions.remove(i)

        return positions

    def move_piece(self, turno):

        cuadro = self.obtener_cuadrado_selecionado()

        if cuadro:

            nombre_pieza = cuadro[0]

            color_pieza = nombre_pieza[:5]

            numero_columna = cuadro[1]

            numero_fila = cuadro[2]

            x, y = self.localizacion_pieza[numero_columna][numero_fila][2]

            if (len(nombre_pieza) > 0) and (color_pieza == turno):
                self.movimientos = self.movimientos_posibles(nombre_pieza, [x, y])

            p = self.localizacion_pieza[numero_columna][numero_fila]

            for i in self.movimientos:
                if i == [x, y]:
                    if (p[0][:5] == turno) or len(p[0]) == 0:
                        self.validar_movimiento([x, y])
                    else:
                        self.capturar_pieza(turno, [numero_columna, numero_fila], [x, y])

            if color_pieza == turno:

                for k in self.localizacion_pieza.keys():
                    for key in self.localizacion_pieza[k].keys():
                        self.localizacion_pieza[k][key][1] = False

                self.localizacion_pieza[numero_columna][numero_fila][1] = True

    def obtener_cuadrado_selecionado(self):
        # get left event
        clic_izquierdo = self.eventos.click_izquierdo()

        if clic_izquierdo:
            # get mouse event
            evento_mouse = self.eventos.get_mouse()

            for i in range(len(self.localizacion_tablero)):
                for j in range(len(self.localizacion_tablero)):
                    rect = pygame.Rect(self.localizacion_tablero[i][j][0], self.localizacion_tablero[i][j][1],
                                       self.tamano_cuadrado, self.tamano_cuadrado)
                    colision = rect.collidepoint(evento_mouse[0], evento_mouse[1])
                    if colision:
                        selected = [rect.x, rect.y]

                        for k in range(len(self.localizacion_tablero)):
                            #
                            try:
                                prueba = None
                                prueba = self.localizacion_tablero[k].index(selected)
                                if prueba is not None:

                                    for val in self.localizacion_pieza.values():
                                        for value in val.values():

                                            if not value[1]:
                                                value[1] = False

                                    columnChar = chr(97 + k)
                                    rowNo = 8 - prueba
                                    # get the name of the
                                    piece_name = self.localizacion_pieza[columnChar][rowNo][0]

                                    return [piece_name, columnChar, rowNo]
                            except:
                                pass
        else:
            return None


    def capture_piece(self, turno, coordenada_tablero, coordenada_pieza):

        x, y = coordenada_pieza


        columnChar, rowNo = coordenada_tablero

        p = self.localizacion_pieza[columnChar][rowNo]

        if p[0] == "rey_blanco":
            self.ganador = "Negras"
            print("Negras ganan")
        elif p[0] == "rey_negro":
            self.ganador = "Blancas"
            print("Blancas ganan")


        self.capturado.append(p)

        self.validar_movimiento(coordenada_pieza)


    def validate_move(self, destino):
        destino_numero_columna = chr(97 + destino[0])
        destino_numero_fila = 8 - destino[1]

        for k in self.localizacion_pieza.keys():
            for key in self.localizacion_pieza[k].keys():
                pieza_en_tablero = self.localizacion_pieza[k][key]

                if pieza_en_tablero[1]:

                    self.localizacion_pieza[k][key][1] = False

                    nombre_pieza = self.localizacion_pieza[k][key][0]

                    self.localizacion_pieza[destino_numero_columna][destino_numero_fila][0] = nombre_pieza

                    buscar_nombre = self.localizacion_pieza[k][key][0]

                    self.localizacion_pieza[k][key][0] = ""


                    if self.turno["negras"]:
                        self.turno["negras"] = 0
                        self.turno["white"] = 1
                    elif "blancas":
                        self.turno["negras"] = 1
                        self.turno["blancas"] = 0


                    buscar_localizacion = k + str(key)
                    buscar_destino = destino_numero_columna + str(destino_numero_fila)
                    print("{} moved from {} to {}".format(buscar_nombre, buscar_localizacion, buscar_destino))


    def diagonal_moves(self, posiciones, nombre_piezas, coordenada_pieza):

        x, y = coordenada_pieza

        while True:
            x = x - 1
            y = y - 1
            if x < 0 or y < 0:
                break
            else:
                posiciones.append([x, y])


            columna_numero = chr(97 + x)
            fila_numero = 8 - y
            p = self.localizacion_pieza[columna_numero][fila_numero]


            if len(p[0]) > 0 and nombre_piezas[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while True:
            x = x + 1
            y = y + 1
            if x > 7 or y > 7:
                break
            else:
                posiciones.append([x, y])


            columna_numero = chr(97 + x)
            fila_numero = 8 - y
            p = self.localizacion_pieza[columna_numero][fila_numero]


            if len(p[0]) > 0 and nombre_piezas[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while True:
            x = x - 1
            y = y + 1
            if x < 0 or y > 7:
                break
            else:
                posiciones.append([x, y])


            columna_numero = chr(97 + x)
            fila_numero = 8 - y
            p = self.localizacion_pieza[columna_numero][fila_numero]


            if len(p[0]) > 0 and nombre_piezas[:5] != p[:5]:
                break


        x, y = coordenada_pieza

        while True:
            x = x + 1
            y = y - 1
            if x > 7 or y < 0:
                break
            else:
                posiciones.append([x, y])


            columna_numero = chr(97 + x)
            fila_numero = 8 - y
            p = self.localizacion_pieza[columna_numero][fila_numero]


            if len(p[0]) > 0 and nombre_piezas[:5] != p[:5]:
                break

        return posiciones