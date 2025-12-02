'''Classe que cuidara do funcionamento da espaconave'''
import pygame

class Ship:
    
    def __init__(self, ai_game):
        '''Inicializa a espaconave e define a posicao inicial'''
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # sobe a imagem da espaconave e obtem seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # comeca cada espaconave nova no centro inferior da tela 
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        '''Desenha a espaconave em sua localizacao atual'''
            
        self.screen.blit(self.image,self.rect)
        
        