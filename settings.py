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
        
        # define a velocidade da espaconave 
        self.ship_speed = 1.5
        
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        
        # define a velocidade do alienigena 
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 
        # fleet direction de 1 representa a direta e -1 representa a esquerda 
        self.fleet_direction = 1 
        
        
        self.pingos_drop_speed = 10 
        
        