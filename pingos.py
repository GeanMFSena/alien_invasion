'''Criando pingos de chuva na tela '''
import pygame 
from pygame.sprite import Sprite


class Pingos(Sprite):
    
    def __init__(self,ai_game):
        super.__init__()
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        
        self.image = pygame.image.load('image/pingos.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        
        self.x = float(self.rect.x)
        
    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom