import sys

import pygame 

def checkEvents(ship): 
    #Movimientos en el teclado o mouse
    #Cada que se haga un movimiento el for se activa
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit()
        
        #Detectar si se presiona la tecla derecha
        elif event.type == pygame.KEYDOWN: 
            #Cuando presionamos cambiamos el movimiento a VERDADERO
            if event.key == pygame.K_RIGHT: 
                ship.moving_right = True 
            elif event.key == pygame.K_LEFT: 
                ship.moving_left = True
        #Cuando soltamos, cambiamos el movimiento a FALSO y se detiene
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_RIGHT: 
                ship.moving_right = False
            elif event.key == pygame.K_LEFT: 
                ship.moving_left = False 

def updateScreen(aiSettings, screen, ship):
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    #Mostramos la pantalla más reciente
    pygame.display.flip() 

