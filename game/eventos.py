import pygame


class Eventos:
    
    def get_mouse(self):
        
        posicion = pygame.mouse.get_pos()
        
        return  posicion
    
    def click_derecho(self):
        
        boton_mouse = pygame.mouse.get_pressed()
        
        click_izquierdo = False 
        
        if boton_mouse[0]:
            click_izquierdo = True
            
        return  click_izquierdo
