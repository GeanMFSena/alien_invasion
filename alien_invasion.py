import sys 
import pygame

class AlienInvasion:
    '''Classe geral para gerenciar ativos e comportamento do jogo'''
    def __init__(self):
        '''Inicializa e cria os arquivos do jogo'''
        pygame.init()
        
        self.screen = pygame.display.set_mode(1200,800)
        pygame.display.set_caption('Alien Invasion')
        
    def run_game(self):
        '''Inicializa o loop principal do jogo'''
        while True:
            # observa os eventos do teclado e do mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                
                # Deixa a tela desenhada mais recente visivel
                pygame.display.flip()
                
                if __name__ == '__main__':
                    # cria uma instancia do jogo e executa o jogo
                    ai = AlienInvasion()
                    ai.run_game()
        