'''Essa classe vai colocar um personagem aleatorio que eu gosto no centro da tela'''
import pygame

class PersonagemAleatorio:
    
    def __init__(self, ai_game):
        '''Inicializa o personagem e define a posicao inicial'''
        
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # sobe a imagem do personagem e obtem seu rect
        self.image = pygame.image.load('images/ship_3.bmp')
        self.rect = self.image.get_rect()
        
        # comeca o personagem no centro da tela 
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        '''Desenha a espaconave em sua localizacao atual'''
            
        self.screen.blit(self.image,self.rect)
        