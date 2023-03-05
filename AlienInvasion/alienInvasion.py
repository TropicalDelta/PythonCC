#Para salir del juego cuando el usuario salga: 
import pygame 

from settings import Settings
from ship import Ship
import gameActions as gf

#Funcion para crear una pantalla y mostrar la pantalla
def runGame(): 
    #Inicializamos todo lo que pygame necesita:
    pygame.init()
    
    #Instanciamos la clase Settings
    aiSettings = Settings()
    #Creamos una pantalla
    screen = pygame.display.set_mode(
        (aiSettings.screen_width, aiSettings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion") 

    #Hacer la nave: 
    ship = Ship(screen)

    #Iniciar el loop para el juego
    while True: 
        #Eventos del juego descritas en gameActions: 
        gf.checkEvents()
        #Características de la pantalla: 
        gf.updateScreen(aiSettings, screen, ship)

runGame()