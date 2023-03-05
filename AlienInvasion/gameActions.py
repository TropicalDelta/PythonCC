import sys

import pygame 

def checkEvents(): 
    #Movimientos en el teclado o mouse
    #Cada que se haga un movimiento el for se activa
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            sys.exit()

def updateScreen(aiSettings, screen, ship):
    screen.fill(aiSettings.bgColor)
    ship.blitme()
    #Mostramos la pantalla más reciente
    pygame.display.flip() 