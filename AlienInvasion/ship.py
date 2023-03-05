import pygame 

class Ship(): 

    def __init__(self, screen): 
        self.screen = screen

        #Cargar la imagen
        self.image = pygame.image.load('AlienInvasion/images/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() 

        #Poner la nave siembre abajo y centro
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self): 
        #Dibuja la nave en la localización dada
        self.screen.blit(self.image, self.rect)