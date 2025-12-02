import sys 
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamento do jogo'''
    
    def __init__(self):
        '''Inicializa e cria os arquivos do jogo'''
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_hight))
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        
        
    def run_game(self):
        '''Inicializa o loop principal do jogo'''
        while True:
            self._chec_events()
            self._update_screen()
            self.clock.tick(60)
        
    def _chec_events(self):  
            # observa os eventos do teclado e do mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
    def _update_screen(self):
        # redesenha a tela durante cada passagem pelo loop
        self.screen.fill(self.settings.bg_color_blue_sky)  
        self.ship.blitme() 
        
        # Deixa a tela desenhada mais recente visivel
        pygame.display.flip()

                
if __name__ == '__main__':
# cria uma instancia do jogo e executa o jogo
    ai = AlienInvasion()
    ai.run_game()
        