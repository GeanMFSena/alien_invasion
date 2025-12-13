import pygame.font

class Scoreboard:
    ''' classe que gera a pontuacao do jogo '''
    
    def __init__(self, ai_game):
        '''inicializa os atributos da pontuacao '''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.settings 
        
        # configuracoes de fonte para informacoes de pontuacao
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        self._prep_score()
        
    def _prep_score(self):
        ''' transforma a pontuacao em uma imagem renderizada '''
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True, self.text_color, self.settings.bg_color)
        
        # exibe a pontuacao no canto superior direito da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =  self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def show_score(self):
        '''desenha a pontuacao na tela '''
        self.screen.blit(self.score_image, self.score_rect)
        
        