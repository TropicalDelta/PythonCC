import pygame 

class Ship(): 

    def __init__(self, aiSettings, screen): 
        self.screen = screen
        self.aiSettings = aiSettings

        #Cargar la imagen
        self.image = pygame.image.load('AlienInvasion/images/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect() 

        #Poner la nave siembre abajo y centro
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False 
        self.moving_left = False

    def update(self): 
        if self.moving_right: 
            self.center += self.aiSettings.ship_speed_factor
        
        if self.moving_left: 
           self.center -= self.aiSettings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self): 
        #Dibuja la nave en la localización dada
        self.screen.blit(self.image, self.rect)