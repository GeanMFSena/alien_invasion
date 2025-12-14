import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    ''' classe que gera a pontuacao do jogo '''
    
    def __init__(self, ai_game):
        '''inicializa os atributos da pontuacao '''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats 
        
        # configuracoes de fonte para informacoes de pontuacao
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        
        self._prep_score()
        self._prep_high_score()
        self._prep_level()
        self._prep_ships()
        
    def _prep_score(self):
        ''' transforma a pontuacao em uma imagem renderizada '''
        rounded_score = round(self.stats.score, -1)
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str,True, self.text_color, self.settings.bg_color)
        
        # exibe a pontuacao no canto superior direito da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =  self.screen_rect.right - 20
        self.score_rect.top = 20
        
    def _prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'{high_score:,}'
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def show_score(self):
        '''desenha a pontuacao na tela '''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
        
    def check_high_score(self):
        '''Verifica se ha uma nova pontuacao maxima'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self._prep_high_score()
            
    
    def _prep_level(self):
        '''Transforma o nivel em uma imagem renderizada '''
        level_str = f'Level: {self.stats.level}'
        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)
        
        '''Posiciona o nivel em baixo da pontuacao '''
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
        
    def _prep_ships(self):
        '''Mostra as espaconaves restantes'''
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10 
            self.ships.add(ship)
            
        
        
        