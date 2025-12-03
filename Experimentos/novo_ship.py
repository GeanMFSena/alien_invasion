'''Classe que cuidara do funcionamento da espaconave'''
import pygame

class Ship:
    
    def __init__(self, ai_game):
        '''Inicializa a espaconave e define a posicao inicial'''
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # sobe a imagem da espaconave e obtem seu rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # comeca cada espaconave nova no centro inferior da tela 
        self.rect.center = self.screen_rect.center
        
        
        # armazena um float com a posicao horizontal exata da espaconave 
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Flag de movimento; comeca com uma espaconave que nao esta se movendo
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        '''Atualiza a posicao da espaconave com base nas flags de movimento'''
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed 
        # atualiza o objeto rect de self.x 
        self.rect.x = self.x 
        self.rect.y = self.y
    
    
    
    def blitme(self):
        '''Desenha a espaconave em sua localizacao atual'''
            
        self.screen.blit(self.image,self.rect)
        
        