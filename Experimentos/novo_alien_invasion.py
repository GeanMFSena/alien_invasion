'''Testes criando um novo alien invasion'''
from novo_settings import Settings  
from novo_ship import Ship
import pygame
import sys 

class NovoAlienInvasion:
    '''Classe geral para gerenciar ativos e comportamento do jogo'''
    
    def __init__(self):
        '''Inicializa e cria os arquivos do jogo'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Novo Alien Invasion')
        self.ship = Ship(self)
        
        
    def run_game(self):
        '''Inicializa o loop principal do jogo'''
        while True:
            self._chec_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
            
    def _chec_events(self):  
        # observa os eventos do teclado e do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._chec_events_keydown(event)
            elif event.type == pygame.KEYUP:
                self._chec_events_keyup(event)
                

    def _chec_events_keydown(self,event):  
        '''Responde as teclas pressionadas'''
        if event.key == pygame.K_RIGHT:
        # move a espaconave para a direita
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
        # move a espaconave para a esquerda
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            # move a espaconave para a cima
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # move a espaconave para a baixo
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

                                          
    def _chec_events_keyup(self, event):
        '''Responde as teclas soltas'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
                    
    def _update_screen(self):
        # redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color_blue_sky)  
        self.ship.blitme() 
        
        # Deixa a tela desenhada mais recente visivel
        pygame.display.flip()

                
if __name__ == '__main__':
# cria uma instancia do jogo e executa o jogo
    ai = NovoAlienInvasion()
    ai.run_game()
        