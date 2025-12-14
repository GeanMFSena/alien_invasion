'''Classe que armazena as configuracoes gerais do jogo'''

class Settings:
    
    def __init__(self):
        '''inicializa as configuracoes do jogo'''
        
        # configuracoes da janela do jogo  
        self.screen_width = 1200
        self.screen_height = 800
        
        # define a cor de background da janela do jogo
        self.bg_color = (230,230,230)
        self.bg_color_blue_sky = (0,169,251)
        
        # aumento de pontos ganhos abatendo alienigenas
        self.score_scale = 1.5
        
        self.ship_limit = 3
        

        self.bullet_width = 3000
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        
       
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.pingos_drop_speed = 10
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        # define a velocidade da espaconave 
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
    
        # define a velocidade do alienigena 
        self.alien_speed = 1.0
        # fleet direction de 1 representa a direta e -1 representa a esquerda 
        self.fleet_direction = 1 
        self.alien_points = 50
        
    def incrase_speed(self):
        '''Aumenta as configuracoes de velocidade '''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale) 
        
     
        
        