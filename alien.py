import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    '''Cria os alienigenas'''
    
    def __init__(self, ai_game):
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect() 
        
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        
        # self.rect.topleft = self.screen_rect.topleft 
        
        self.rect.x = self.screen.width
        self.rect.y = self.screen.height
        
        self.x = float(self.rect.x)
        
        