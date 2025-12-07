'''Cria estrelas '''

import pygame
from pygame.sprite import Sprite


class Stars(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        # Pegando o tamanho da tela do Alien Invasion
        self.screen = ai_game.screen
        # Pegando o rect da tela 
        self.screen_rect = ai_game.screen.get_rect()
        
        # pegando a imagem das estrelas e o rect dela 
        self.image = pygame.image.load('images/Estrela_negra_fundo_branco pequeno.png')
        self.rect = self.image.get_rect()
        
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        