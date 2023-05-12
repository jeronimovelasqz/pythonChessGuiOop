import pygame


class Eventos:

    def get_mouse(self):
        posicion = pygame.mouse.get_pos()

        return posicion

    def click_derecho(self):
        boton_mouse = pygame.mouse.get_pressed()

        click_izquierdo = False

        if boton_mouse[0]:
            click_izquierdo = True

        return click_izquierdo


    def click_izquierdo(self):

        boton_mouse = pygame.mouse.get_pressed()

        click_izquiedo = False

        if boton_mouse[0]:

            click_izquiedo = True

        return click_izquiedo
